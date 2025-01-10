from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    """ 
    Notification serializer. Validates the 'topic' and 'description' fields.

    The 'topic' field is required
    The 'description' field is required and must be a string with a maximum length of 1000 characters.
    """

    topic = serializers.CharField(required=True,)
    description = serializers.CharField(required=True, max_length=1000)

    # Could include additional validations (e.g. regex, etc.) depending on the requirements.
