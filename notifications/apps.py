from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        '''
        This method is called when the app is ready.
        We use it to register the notifiers in the factory.
        '''
        from .factories import notifier_factory
        from .notifiers import SlackNotifier, EmailNotifier

        notifier_factory.register("sales", SlackNotifier)
        notifier_factory.register("pricing", EmailNotifier)

        # We could add more topics in the future
        # notifier_factory.register("support", WhatsAppNotifier)
