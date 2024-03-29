"""
Django settings.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from peach.conf.base import *

ENVIRONMENT = "local"
DEBUG = True
SILKY_PYTHON_PROFILER = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'peach',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'request_id': {
#                 '()': 'log_request_id.filters.RequestIDFilter'
#         },
#     },
#     'formatters': {
#             'verbose': {
#                 'format': "[%(asctime)s] %(levelname)s [%(request_id)s] [%(name)s:%("
#                           "lineno)s] %(""message)s",
#                 'datefmt': "%d/%b/%Y %H:%M:%S"
#             },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'filters': ['request_id'],
#             'formatter': 'verbose',
#         },
#         'application': {
#                 'level': 'DEBUG',
#                 'class': 'logging.handlers.TimedRotatingFileHandler',
#                 'when': 'midnight',
#                 'backupCount': 3,
#                 'filename': 'logs/peach.log',
#                 'formatter': 'verbose',
#                 'filters': ['request_id'],
#             },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'application'],
#         },
#     }
# }
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

DOMAIN = 'localhost:3000'
LOG_RESPONSE = False
LOG_REQUEST = False

# EMAIL_HOST_USER = 'shekharkhanna.sovk@gmail.com'
# EMAIL_HOST_PASSWORD = 'sksovk123'