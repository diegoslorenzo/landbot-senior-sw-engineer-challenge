from django.db import models

class Notification(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_SENT = 'sent'
    STATUS_FAILED = 'failed'
    
    topic = models.CharField(max_length=50) # "sales", "pricing", etc.
    description = models.TextField()
    status = models.CharField(max_length=20, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    attempts = models.PositiveIntegerField(default=0) # Number of attempts to send the notification (for example, useful for knowing when to give up or retry)

    def __str__(self):
        return f"[{self.id}] {self.topic} - {self.status}"
