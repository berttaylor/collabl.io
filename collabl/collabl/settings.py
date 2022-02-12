"""
Django settings for collabl project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import json
import os
from datetime import timedelta
from distutils.util import strtobool
from pathlib import Path

import sentry_sdk
import storages.backends.s3boto3
from celery.schedules import crontab
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
# CHANGED - SENT SECRET KEY TO ENV
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = bool(strtobool(os.environ.get("DJANGO_DEBUG_STATUS")))
ALLOWED_HOSTS = json.loads(os.environ.get("DJANGO_ALLOWED_HOSTS"))

# ADDED: More constants
# Used as a constant for various references around the system
SITE_PROTOCOL = os.environ.get("SITE_PROTOCOL")
SITE_DOMAIN = os.environ.get("SITE_DOMAIN")
DEFAULT_SYSTEM_FROM_EMAIL = os.environ.get("DEFAULT_SYSTEM_FROM_EMAIL")
DEFAULT_SYSTEM_TO_EMAIL = os.environ.get("DEFAULT_SYSTEM_TO_EMAIL")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_SYSTEM_FROM_EMAIL")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "collaborations",
    "groups",
    "support",
    "chat",
    "storages",
    "django_htmx",
    "axes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "collabl.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(os.path.join(BASE_DIR, "templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "groups.context_processors.group_views_context",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "collabl.wsgi.application"

# CHANGED: Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_DB_HOST"),
        "PORT": os.environ.get("POSTGRES_DB_PORT"),
    },
}

# ADDED: SMTP details for mail sending
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")

# ADDED: We use BCrypt as default here
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]

# ADDED: Celery configuration
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_TIMEZONE = os.environ.get("CELERY_TIMEZONE")
CELERY_TASK_SERIALIZER = os.environ.get("CELERY_TASK_SERIALIZER")
CELERY_RESULT_SERIALIZER = os.environ.get("CELERY_RESULT_SERIALIZER")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_IMPORTS = ("collabl.tasks",)

# ADDED: Storage Config
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_ADDRESSING_STYLE = "virtual"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ADDED: Override Authentication_backends
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    # Django ModelBackend is the default authentication backend.
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# ADDED: Points to our custom user model
AUTH_USER_MODEL = "users.User"

# CHANGED: Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")  # Added
MEDIA_ROOT = os.path.join(BASE_DIR, "media/root")  # Added

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ADDED: Set some URLs and overrides
LOGIN_URL = "/login/"
LOGOUT_REDIRECT_URL = "/login/"
LOGIN_REDIRECT_URL = "/user/collaborations/"

# ADDED: Axes settings
AXES_FAILURE_LIMIT = 10  # Number of failed attempts before lockout
AXES_COOLOFF_TIME = 2  # If integer, in hours
AXES_RESET_ON_SUCCESS = (
    True  # If True, a successful login will reset the number of failed logins
)
AXES_ONLY_ADMIN_SITE = False  # Handle both admin panel and regular logins
AXES_ENABLE_ADMIN = True  # Allow admin management