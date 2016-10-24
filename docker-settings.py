# Importing common provides default settings, see:
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_DB_NAME'),
        'HOST': os.getenv('POSTGRES_PORT_5432_TCP_ADDR') or os.getenv('TAIGA_DB_HOST'),
        'USER': os.getenv('TAIGA_DB_USER'),
        'PASSWORD': os.getenv('POSTGRES_ENV_POSTGRES_PASSWORD') or os.getenv('TAIGA_DB_PASSWORD')
    }
}

TAIGA_HOSTNAME = os.getenv('TAIGA_HOSTNAME')

SITES['api']['domain'] = TAIGA_HOSTNAME
SITES['front']['domain'] = TAIGA_HOSTNAME

MEDIA_URL  = 'http://' + TAIGA_HOSTNAME + '/media/'
STATIC_URL = 'http://' + TAIGA_HOSTNAME + '/static/'

if os.getenv('TAIGA_SSL').lower() == 'true':
    SITES['api']['scheme'] = 'https'
    SITES['front']['scheme'] = 'https'

    MEDIA_URL  = 'https://' + TAIGA_HOSTNAME + '/media/'
    STATIC_URL = 'https://' + TAIGA_HOSTNAME + '/static/'

SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')

if os.getenv('RABBIT_PORT') is not None and os.getenv('REDIS_PORT') is not None:
    from .celery import *

    BROKER_URL = 'amqp://guest:guest@rabbit:5672'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERY_ENABLED = True

    EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
    EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://guest:guest@rabbit:5672"}


#########################################
## GENERIC
#########################################
#MEDIA_ROOT = '/home/taiga/media'
#STATIC_ROOT = '/home/taiga/static'

#########################################
## MAIL SYSTEM SETTINGS
#########################################

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds

EMAIL_USE_TLS = False
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# EMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

# GMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'youremail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'


#########################################
## REGISTRATION
#########################################

#PUBLIC_REGISTER_ENABLED = True

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
if os.getenv('GITHUB_URL'):
    GITHUB_URL = os.getenv('GITHUB_URL')
    GITHUB_API_URL = os.getenv('GITHUB_API_URL')
    GITHUB_API_CLIENT_ID = os.getenv('GITHUB_API_CLIENT_ID')
    GITHUB_API_CLIENT_SECRET = os.getenv('GITHUB_API_CLIENT_SECRET')

#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

#STATS_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
## CELERY
#########################################

from .celery import *
BROKER_URL = 'amqp://guest:guest@celery:5672//'
CELERY_RESULT_BACKEND = 'redis://celery:6379/0'
CELERY_ENABLED = True

# To use celery in memory
#CELERY_ENABLED = True
#CELERY_ALWAYS_EAGER = True
