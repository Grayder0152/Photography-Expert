import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-j=ri%2mtysssz-isic%23e!#gi-hg*dh5gecrje*3v+%dy#sxo-si+%3n@'

DEBUG = True

ALLOWED_HOSTS = ['photography-expert.herokuapp.com', '127.0.0.1', '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup',
    'main',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Photography_Expert.urls'

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddk6ctr801f4aa',
        'USER': 'sluldompbnthaf',
        'PASSWORD': 'cd469468311439312553c0061cc99a0155dabfc057868677ab30da3f1cefbaf8',
        'HOST': 'ec2-52-205-3-3.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

WSGI_APPLICATION = 'Photography_Expert.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddk6ctr801f4aa',
        'USER': 'sluldompbnthaf',
        'PASSWORD': 'cd469468311439312553c0061cc99a0155dabfc057868677ab30da3f1cefbaf8',
        'HOST': 'ec2-52-205-3-3.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_ACCESS_KEY_ID = 'AKIAQWPVTWVA6HW7H74K'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'phtography-expert'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'Photography_Expert.storages.MediaStorage'
