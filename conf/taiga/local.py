# If you want to modify this file, I recommend check out docker-taiga-example
# https://github.com/benhutchins/docker-taiga-example
#
# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py

# Importing common provides default settings, see:
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .common import *

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

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
TAIGA_HOST = os.getenv('TAIGA_HOST')
TAIGA_PORT = os.getenv('TAIGA_PORT')

SITES['api']['domain'] = TAIGA_HOSTNAME
SITES['front']['domain'] = TAIGA_HOSTNAME
MEDIA_URL  = 'http://' + TAIGA_HOSTNAME + '/media/'
STATIC_URL = 'http://' + TAIGA_HOSTNAME + '/static/'

if os.getenv('TAIGA_SSL'):
    SITES['api']['scheme'] = 'https'
    SITES['front']['scheme'] = 'https'
    MEDIA_URL  = 'https://' + TAIGA_HOSTNAME + '/media/'
    STATIC_URL = 'https://' + TAIGA_HOSTNAME + '/static/'

if os.getenv('TAIGA_SECRET_KEY'):
    SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

if os.getenv('EMAIL_USE_HOSTIP'):
    EMAIL_HOST = os.getenv('HOSTIP')
else:
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

# To use celery in memory
#CELERY_ENABLED = True
#CELERY_ALWAYS_EAGER = True


# print("DATABASES:\n" + DATABASES)
# print("SITES:\n" + SITES)
print("TAIGA_HOSTNAME: " + TAIGA_HOSTNAME)
print("TAIGA_HOST: " + TAIGA_HOST)
print("TAIGA_PORT: " + TAIGA_PORT)

print("MEDIA_URL: " + MEDIA_URL)
print("STATIC_URL: " + STATIC_URL)

if EMAIL_USE_TLS:
    print("EMAIL_USE_TLS: " + EMAIL_USE_TLS)

if EMAIL_HOST:
    print("EMAIL_HOST: " + EMAIL_HOST)

if EMAIL_PORT:
    print("EMAIL_PORT: " + EMAIL_PORT)

if EMAIL_HOST_USER:
    print("EMAIL_HOST_USER: " + EMAIL_HOST_USER)

if EMAIL_HOST_PASSWORD:
    print("EMAIL_HOST_PASSWORD: " + EMAIL_HOST_PASSWORD)

