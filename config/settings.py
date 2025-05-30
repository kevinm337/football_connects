from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']  # dev/CI; tighten later

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'community','scores','interaction','fantasy','predictions',
]

MIDDLEWARE = [ ... ]  # keep default

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST','localhost')}:{config('DB_PORT','5432')}/{config('DB_NAME')}"
    )
}

CACHES = {
    "default": {
        "BACKEND":"django_redis.cache.RedisCache",
        "LOCATION":config("REDIS_URL","redis://127.0.0.1:6379/1"),
        "OPTIONS":{"CLIENT_CLASS":"django_redis.client.DefaultClient"}
    }
}

# rest unchanged…
