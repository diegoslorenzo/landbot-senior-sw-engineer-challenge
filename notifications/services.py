from django_q.tasks import async_task

from .interfaces import NotificationOrchestratorInterface
from .tasks import process_notification

class DjangoQNotificationOrchestrator(NotificationOrchestratorInterface):
    """
    DjangoQ implementation of the NotificationOrchestratorInterface.
    """
    def enqueue_notification(self, notification_id: int) -> None:
        async_task(process_notification, notification_id)


notification_orchestrator = DjangoQNotificationOrchestrator()
