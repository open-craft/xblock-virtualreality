"""
Django settings for the xblock-chat project.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This is just a container for running tests, it's okay to allow it to be
# defaulted here if not present in environment settings
SECRET_KEY = os.environ.get('SECRET_KEY', '",cB3Jr.?xu[x_Ci]!%HP>#^AVmWi@r/W3u,w?pY+~J!R>;WN+,3}Sb{K=Jp~;&k')

# SECURITY WARNING: don't run with debug turned on in production!
# This is just a container for running tests
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'statici18n',
    'virtualreality',
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'virtualreality/translations'),
]

# statici18n
# http://django-statici18n.readthedocs.io/en/latest/settings.html

with open(os.path.join(BASE_DIR, 'virtualreality/translations/config.yaml'), 'r') as locale_config_file:
    LOCALE_CONFIG = yaml.load(locale_config_file)

    LANGUAGES = [
        (code, code,)
        for code in LOCALE_CONFIG['locales'] + LOCALE_CONFIG['dummy_locales']
    ]

STATICI18N_DOMAIN = 'textjs'

STATICI18N_NAMESPACE = 'VirtualRealityXBlockI18N'
STATICI18N_PACKAGES = (
    'virtualreality',
)
STATICI18N_ROOT = 'virtualreality/public/js'
STATICI18N_OUTPUT_DIR = 'translations'
