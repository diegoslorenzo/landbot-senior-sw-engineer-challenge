from django_q.tasks import async_task
from django.db import transaction

from .models import Notification
from .factories import notifier_factory

def process_notification(notification_id: int):
    """
    Real logic for sending: fetches the notification from the DB,
    sends it through the corresponding channel and updates status (sent/failed).
    """
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        print(f"Notification {notification_id} does not exist.")
        return

    if notification.status == Notification.STATUS_SENT:
        print(f"Notification {notification_id} already sent.")
        return

    with transaction.atomic():
        notification.attempts += 1
        notification.save()

        notifier = notifier_factory.get_notifier(notification.topic)
        if not notifier:
            print(f"Notifier not found for topic {notification.topic}")
            notification.status = Notification.STATUS_FAILED
            notification.save()
            return

        try:
            notifier.notify(notification.description)
            notification.status = Notification.STATUS_SENT
            notification.save()
            print(f"Notification {notification_id} sent successfully.")
        except Exception as e:
            notification.status = Notification.STATUS_FAILED
            notification.save()
            print(f"Error sending notification {notification_id}: {e}")
