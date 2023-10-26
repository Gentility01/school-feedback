from .base import *
import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', 'aefunai-feedbacks.onrender.com']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
