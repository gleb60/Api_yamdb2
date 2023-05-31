import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
