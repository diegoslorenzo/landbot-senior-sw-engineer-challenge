from django.test import TestCase
from unittest.mock import patch
from django.core import mail

from .notifiers import EmailNotifier

from .models import Notification
from .tasks import process_notification

class EmailNotifierTest(TestCase):
    def test_email_notifier_sends_to_memory(self):
        """
        Test that the email notifier sends an email to memory.
        """
        notifier = EmailNotifier()
        notifier.notify("Test message - Pricing")

        # Check that the email was sent
        self.assertEqual(len(mail.outbox), 1) # It should have sent 1 email in memory

        sent_email = mail.outbox[0] # Get the first email sent
        self.assertIn("Test message - Pricing", sent_email.body)
        self.assertEqual(sent_email.subject, "Notification from bot")
        self.assertEqual(sent_email.from_email, "noreply@myproject.com")
        self.assertEqual(sent_email.to, ["pricing@myproject.com"])

    def test_process_notification_email_success(self):
        # Creamos una notificación
        notif = Notification.objects.create(
            topic="pricing",
            description="Test pricing"
        )
        # Llamamos directamente a process_notification (sin colas)
        process_notification(notif.id)

        notif.refresh_from_db() # Refresh the object from the database
        self.assertEqual(notif.status, Notification.STATUS_SENT)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Test pricing", mail.outbox[0].body)


    @patch("notifications.notifiers.send_mail", side_effect=Exception("SMTP Error")) # side_effect: A parameter that allows to raise an exception when the function is called.
    def test_email_notify_exception_handled(self, mock_send_mail):
        """ 
        Test that the email notifier handles exceptions when sending an email.

        mock_send_mail: A mock object that replaces the send_mail function with side_effect (the mock object).
        """
        notifier = EmailNotifier()
        notifier.notify("Test message - Pricing")

        # Check that the email was not sent
        self.assertEqual(len(mail.outbox), 0) # it should not send any email if it fails
