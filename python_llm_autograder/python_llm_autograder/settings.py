"""
Django settings for python_llm_autograder project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*2(aye!$1!oa(5)p=)jmk&^yurhm$h&l5mgfw+9+k4+2f^7o%b"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    "grading.apps.GradingConfig",
    # "grading",
    "analytics",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "crispy_forms",
    "crispy_bootstrap5",
    # 'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'django_pandas',
    # 'dpd_static_support',
    # 'channels',
    # 'channels_redis',
    # "ckeditor",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # 'django_plotly_dash.middleware.BaseMiddleware',
    # 'django_plotly_dash.middleware.ExternalRedirectionMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

ROOT_URLCONF = "python_llm_autograder.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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
# ASGI_APPLICATION = 'python_llm_autograder.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',  # Use RedisChannelLayer for production
#     },
# }

WSGI_APPLICATION = "python_llm_autograder.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.mysql",
        "NAME": "autograder_job",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT":3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'grading.Lecturer'
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT =  BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / 'grading' / 'static',
    ]
# STATICFILES_FINDERS = [

#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',

#     'django_plotly_dash.finders.DashAssetFinder',
#     'django_plotly_dash.finders.DashComponentFinder',
#     'django_plotly_dash.finders.DashAppDirectoryFinder',
# ]

# PLOTLY_COMPONENTS = [
#     'dash',
#     'dash.dcc',  # dash_core_components
#     'dash.html',  # dash_html_components
#     'dash.dependencies',  # dash_renderer
#     'dash_bootstrap_components',
#     'dpd_components',
#     'dpd_static_support',
#     'dash_bootstrap_components',
# ]
# PLOTLY_COMPONENTS = [

#     # Common components (ie within dash itself) are automatically added

#     # django-plotly-dash components
#     'dpd_components',
#     # static support if serving local assets
#     'dpd_static_support',

#     # Other components, as needed
#     'dash_bootstrap_components',
# ]

# PLOTLY_DASH = {
#     "inject_html": False,  # Disable live updates
#     "suppress_callback_exceptions": True,
#     "serve_locally": True,
#     "stateless_loader": True
# }

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "grading-home"
LOGOUT_REDIRECT_URL = "grading-home"

MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = 'media/'

# PLOTLY_DASH = {
#     'cache_timeout': 60,
# }
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     },
# }