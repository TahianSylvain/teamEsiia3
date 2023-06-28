import json
import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

with open('jsonForce.json') as secret_file:
    config = json.load(secret_file)
    SECRET_KEY = config['secret_file']

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '*',
    '127.0.0.1',
    '169.254.138.114',
    '169.254.242.95',
    '192.168.137.1',
    '192.168.43.14',
    '192.168.248.14',
    '192.168.19.14',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'accounts',
    'department',
    'course',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'axes.middleware.AxesMiddleware',
]

# AXES_LOCK_OUT_AT_FAILURE = False
# AXES_USE_USER_AGENT = True
# AXES_COOLOFF_TIME = 1
# AXES_LOGIN_FAILURE_LIMIT = 5
# AXES_ONLY_USER_FAILURES = True


ROOT_URLCONF = 'lvlind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "lvlind/templates")],
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

WSGI_APPLICATION = 'lvlind.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation   https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT-3'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = "d M Y -- H:m:s"

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

LOGIN_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.MyUser'
