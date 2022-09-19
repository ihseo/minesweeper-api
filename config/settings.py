import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'randomlygenerated-@ga^2po&_&70jg43g!waj!%fisuup2b0n=-lhh@))e8!8vi5b-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not os.environ.get('PRODUCTION')

ALLOWED_HOSTS = ['*']
# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'rest_framework',
    'drf_yasg',
    'corsheaders',
]

INTERNAL_APPS = [
    'core',
]

INSTALLED_APPS = INTERNAL_APPS + EXTERNAL_APPS + DJANGO_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS control
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# if os.environ.get('PRODUCTION'):
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
# AUTH_USER_MODEL = 'user.User'

# Rest Framework Authentication Classes
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "config.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    # "DEFAULT_PAGINATION_CLASS": "core.pagination.DefaultPagination",
    # 'PAGE_SIZE': 10
}

# AWS Config
AWS_ACCESS_KEY_ID = '*********************************'
AWS_SECRET_ACCESS_KEY = '*********************************'

# Celery Config
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
# CELERY_BROKER_URL = 'redis://redis:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE  # Celery Beats에서 사용할 Time Zone
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60

# Celery SQS Config
# sqs_aws_access_key = safequote(AWS_ACCESS_KEY_ID)
# sqs_aws_secret_key = safequote(AWS_SECRET_ACCESS_KEY)
# CELERY_PAYMENT_BROKER_URL = f"sqs://{sqs_aws_access_key}:{sqs_aws_secret_key}@"
# CELERY_PAYMENT_BROKER_TRANSPORT_OPTIONS = {'region': 'ap-northeast-2'}
# CELERY_PAYMENT_ACCEPT_CONTENT = ['json']
# CELERY_PAYMENT_TASK_SERIALIZER = 'json'
# CELERY_PAYMENT_TIMEZONE = TIME_ZONE  # Celery Beats에서 사용할 Time Zone
# CELERY_PAYMENT_TASK_TRACK_STARTED = True
# CELERY_PAYMENT_TASK_TIME_LIMIT = 30 * 60

# Email Config (AWS SES)
AWS_SES_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SES_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY

# S3 File Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = '**********'
AWS_S3_CUSTOM_DOMAIN = '***********'

# CORS Control
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8000',
)

# Swagger Auth
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    # "exclude_names": ['account', 'register', 'kakao_login',],    #  List URL namespaces to ignore
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# QEncode API Key
# QENCODE_API_KEY = '************'

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

