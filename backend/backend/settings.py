import os
from pathlib import Path
from corsheaders.defaults import default_headers
from . import database  # Ensure you have `database.py` configured

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep this secret key safe in production!
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-8^fq+a!kh-4pm8#y(urc^&zum$01nvb69$s=vnif(#gn6o7)_!'
)

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

# Allowed hosts - Use '*' for local dev, restrict in production
ALLOWED_HOSTS = ['*']

# Installed apps
INSTALLED_APPS = [
    'api',
    'shifts',
    'inventory',
    'posFin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Must be above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# CORS settings
CORS_ALLOW_CREDENTIALS = True  # Allow credentials (cookies, sessions)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vue app on Vite dev server
    "http://127.0.0.1:8000",
]
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
    'content-type',
    'authorization',
]
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

SESSION_COOKIE_SAMESITE = 'Lax'  # ✅ Allows cookies in cross-site requests
CSRF_COOKIE_SAMESITE = 'Lax'  # Ensures CSRF token is sent

CSRF_COOKIE_NAME = "csrftoken"  # Default Django CSRF cookie name
CSRF_COOKIE_HTTPONLY = False  # Ensure it's readable by JavaScript
CSRF_COOKIE_SECURE = False  # Set to True in production with HTTPS

# Internal network settings (for debugging)
INTERNAL_IPS = ['127.0.0.1']

# URL configuration
ROOT_URLCONF = 'backend.urls'

# Templates configuration
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

# WSGI application

# Authentication settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Custom user model
AUTH_USER_MODEL = 'api.User'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # Uses Django session-based auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Ensures user must be authenticated
    ],
}

# Database configuration
DATABASES = {
    'default': database.config()
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Login & logout redirection
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
