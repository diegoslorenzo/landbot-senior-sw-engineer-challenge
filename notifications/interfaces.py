from abc import ABC, abstractmethod

class NotificationOrchestratorInterface(ABC):
    """
    Interface for a notification orchestrator
    """
    @abstractmethod
    def enqueue_notification(self, notification_id: int) -> None:
        pass
