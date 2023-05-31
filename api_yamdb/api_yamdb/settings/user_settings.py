import os
from dotenv import load_dotenv


load_dotenv()

# Так, как без .env не проходят тесты яндекса:

SECRET_KEY = os.getenv('KEY', '123456789')

DEBUG = os.getenv('DEBUG', 'FALSE')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
