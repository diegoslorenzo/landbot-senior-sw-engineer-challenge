from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import NotificationSerializer
from notifications.models import Notification
from notifications.services import notification_orchestrator
from notifications.factories import notifier_factory

class NotifyAPIView(APIView):
    """
    Recive a JSON with 'topic' and 'description'.
    Uses the factory to get the channel.
    Enqueues the notification to be sent.
    """

    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        topic = serializer.validated_data['topic']
        description = serializer.validated_data['description']

        # Verify if the topic is registered
        notifier = notifier_factory.get_notifier(topic)
        if not notifier:
            # Return 404 and not send the notification
            return Response(
                {"message": f"Topic '{topic}' not registered."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        print(f"Creating notification with topic '{topic}' in DB")
        # Create the notification in DB
        notification = Notification.objects.create(
            topic=topic,
            description=description,
            # status=Notification.Status.PENDING
        )
    
        # Enqueue the notification to be sent
        notification_orchestrator.enqueue_notification(notification.id)

        return Response(
            {"message": f"Notification sent successfully."},
            status=status.HTTP_200_OK
        )
