from typing import Optional
from .notifiers import BaseNotifier

class NotifierFactory:
    """
    Factory that resolves a 'topic' and returns the corresponding notifier.
    Registration is done through an internal dict.
    """
    def __init__(self):
        self._registry = {}  # dict: topic -> NotifierClass

    def register(self, topic: str, notifier_class: type[BaseNotifier]):
        """Registers a topic with its notifier class."""
        self._registry[topic.lower()] = notifier_class # Lowercase the topic for case-insensitive matching

    def get_notifier(self, topic: str) -> Optional[BaseNotifier]:
        """ Returns notifier instance for the topic """
        notifier_class = self._registry.get(topic.lower()) # Lowercase the topic for case-insensitive matching
        if not notifier_class:
            return None
        return notifier_class()


# We create a global instance of the factory (could live in a global module).
# Alternatively, you could make the factory get its configuration from a JSON file, the database, etc.
notifier_factory = NotifierFactory()
# The important thing is that it is extensible without touching the endpoint.
