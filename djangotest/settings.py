"""
Django settings for djangotest project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ubm_gmo=4d8t7=@!vhb_vn1d4=mqn!uid$8f8tly4%l2!sqz8l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'learn',
    'DjangoUeditor',
#    'users',
]
#AUTH_USER_MODEL = 'users.User'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangotest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
# TEMPLATE_CONTEXT_PROCESSORS=(
#     "django.core.context_processors.request",
# )

WSGI_APPLICATION = 'djangotest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.mysql',
    #     'NAME': 'djangotest',
    #     'USER': 'root',
    #     'PASSWORD': 'liuzhen',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # },
    'default': {
        'NAME': 'DTcmsdb3',
        'ENGINE': 'sql_server.pyodbc',
        #'django.db.backends.sqlserver_ado',
        'HOST': '(local)',
        'USER': 'sa',
        'PASSWORD': 'Password01!',
        'OPTIONS': {
            'provider': 'SQLOLEDB', # Have also tried 'SQLCLI11' and 'SQLOLEDB'
            'extra_params': 'DataTypeCompatibility=80'
            },
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

#LANGUAGE_CODE = 'en'
LANGUAGE_CODE = 'zh_hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}

USERS_REGISTRATION_OPEN = True

USERS_VERIFY_EMAIL = True

USERS_AUTO_LOGIN_ON_ACTIVATION = True

USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3

# Specifies minimum length for passwords:
USERS_PASSWORD_MIN_LENGTH = 5

# Specifies maximum length for passwords:
USERS_PASSWORD_MAX_LENGTH = None

# the complexity validator, checks the password strength
USERS_CHECK_PASSWORD_COMPLEXITY = True

USERS_SPAM_PROTECTION = False  # important!

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'zliu@eco-edu.cn'
EMAIL_HOST_PASSWORD = 'liuzhen83'
DEFAULT_FROM_EMAIL = 'zliu@eco-edu.cn'