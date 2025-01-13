# config/settings/production.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'email@gmail.com')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@gmail.com')
# NOTIFICATION_EMAIL = os.environ.get('NOTIFICATION_EMAIL', 'pricing@gmail.com') # Who will receive the notifications for "pricing", for example

# Aditional configuration for production
