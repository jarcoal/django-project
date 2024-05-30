"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import sys
from pathlib import Path
from urllib.parse import urlencode

import environ

# Configure env defaults
env = environ.Env(
    # Interpret as boolean, default to False
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "local"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
ENVIRONMENT = env("ENVIRONMENT")

TESTING = "test" in sys.argv

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Us
    "app",
    # 3rd Party
    "django_otp",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_hotp",
    "django_otp.plugins.otp_static",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.microsoft",
    "rest_framework",
    "corsheaders",
    "anymail",
    "ordered_model",
    "django_celery_results",
    "django_celery_beat",
    "safedelete",
    "oauth2_provider",  # make sure this comes after "app" so we can override templates
    "webpack_loader",
    "django_recaptcha",
]

if not TESTING:
    INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

if not TESTING:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env.db()}

# Cache
# https://docs.djangoproject.com/en/3.2/ref/settings/#caches
CACHES = {"default": env.cache("REDIS_URL")}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Auth

AUTH_USER_MODEL = "app.User"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# OAuth2 Toolkit
OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 86400 * 365,
}

# URL of the post-login dashboard.  We use this for our OAuth2 application
OAUTH2_APPLICATION_NAME = env("OAUTH2_APPLICATION_NAME", default="Dashboard")
OAUTH2_APPLICATION_REDIRECT_URI = env(
    "OAUTH2_APPLICATION_REDIRECT_URI", default="/dashboard/"
)

OTP_TOTP_ISSUER = "Django app"

DASHBOARD_URL = env("DASHBOARD_URL")
DASHBOARD_CLIENT_ID = env("DASHBOARD_CLIENT_ID")

LOGIN_REDIRECT_URL = "/oauth/authorize/?" + urlencode(
    {
        "client_id": DASHBOARD_CLIENT_ID,
        "redirect_uri": DASHBOARD_URL,
        "grant_type": "authorization_code",
        "response_type": "token",
        "scope": "read write",
    }
)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configure Email

EMAIL_BACKEND = "anymail.backends.amazon_ses.EmailBackend"

ANYMAIL = {}

# Celery

CELERY_BROKER_URL = env("REDIS_URL")
CELERY_RESULT_BACKEND = "django-db"

CELERY_QUEUES = []

# Django-debug-toolbar

ENABLE_DEBUG_TOOLBAR = env("ENABLE_DEBUG_TOOLBAR", default=False)

DEBUG_TOOLBAR_CONFIG = {
    "RESULTS_CACHE_SIZE": 100,
    "SHOW_TOOLBAR_CALLBACK": lambda req: ENABLE_DEBUG_TOOLBAR and req.user.is_superuser,
}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    # 'debug_toolbar.panels.settings.SettingsPanel',
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Logging

LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
GENERATE_REQUEST_ID_IF_NOT_IN_HEADER = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "request_id": {"()": "log_request_id.filters.RequestIDFilter"},
    },
    "formatters": {
        "json": {
            "()": "app.utils.log.JsonFormatter",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG" if DEBUG else "INFO",
            "class": "logging.StreamHandler",
            "filters": ["request_id"],
            "formatter": "json",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


# Recaptcha
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")


# Rate-limiting

LOGIN_RATELIMIT_PER_SECOND = env("LOGIN_RATELIMIT_PER_SECOND", default="3/s")
LOGIN_RATELIMIT_PER_HOUR = env("LOGIN_RATELIMIT_PER_HOUR", default="50/h")
