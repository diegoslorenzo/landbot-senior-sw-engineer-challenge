from abc import ABC, abstractmethod
import os
import requests
import logging

from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

class BaseNotifier(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass

class SlackNotifier(BaseNotifier):
    def notify(self, message: str) -> None:
        logger.info(f"[MOCK SLACK] Notifiying: {message}")


class EmailNotifier(BaseNotifier):
    """
    Sends an email notification to the configured email address
    """
    def notify(self, message: str) -> None:
        try:
           send_mail(
                subject="Notification from bot",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFICATION_EMAIL],
                fail_silently=False # if True, exceptions are silenced
            )
        except Exception as e:
            # TODO: Handle the error properly 
            logger.info(f"Error sending email notification: {e}")
