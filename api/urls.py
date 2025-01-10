from django.urls import path
from .views import NotifyAPIView

urlpatterns = [
    path('notify/', NotifyAPIView.as_view(), name='notify'),
]
