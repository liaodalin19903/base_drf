"""
Django settings for base_drf project.

Generated by 'django-admin startproject' using Django 3.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 2

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mz3+-9k3#89@2tmr(o+h#!nk)0b*2z^75ak-7i4kl*sk7#=%a9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1',
    'http://127.0.0.1:8000',

    'http://10.10.10.102',
    'http://10.10.10.102:8000', # 官网
    'http://10.10.10.102:8080', # 管理员后台
    'http://10.10.10.102:8081',
    'http://10.10.10.102:8888',

    'http://10.10.10.103',
    'http://10.10.10.103:8000',
    'http://10.10.10.103:8080',
    'http://10.10.10.103:8081',
    'http://10.10.10.103:8888',

    'http://10.10.10.105:8000',
    'http://10.10.10.105:8001',
    'http://10.10.10.105:8080',
    'http://10.10.10.105:8888',

    'http://0.0.0.0',
    'http://0.0.0.0:8000',
    'http://0.0.0.0:8001',
    'http://0.0.0.0:8080',
    'http://0.0.0.0:8888',

    'http://localhost:8888'
)


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'django.contrib.sites',

    'corsheaders', # 跨域头

    'rest_framework',

    'rest_framework.authtoken',

    'rest_framework_swagger',

    'rest_auth',

    #'account',

    'allauth',

    'allauth.account',

    'allauth.socialaccount',

    'rest_auth.registration',

    'base_drf',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'base_drf.middlewares.AccessControlMiddleware.AccessControl'
]

ROOT_URLCONF = 'base_drf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'base_drf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

   'default': {

       'ENGINE': 'django.db.backends.mysql',

       'NAME': 'base_drf',

       'USER':'root',

       'PASSWORD':'devops',

       'HOST':'127.0.0.1',

       'PORT':'3306',

       'OPTIONS' : {

          'init_command' : '''

                SET NAMES utf8;

                SET CHARACTER SET utf8;

                SET character_set_connection=utf8;'''

        },

   }

}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'


TIME_ZONE = 'Asia/Shanghai'


USE_L10N = True


USE_TZ = True


USE_I18N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True
}




