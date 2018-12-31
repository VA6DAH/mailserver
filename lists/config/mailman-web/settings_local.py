EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '172.19.199.1'
EMAIL_PORT = 25

INSTALLED_APPS = (
    'hyperkitty',
    'postorius',
    'django_mailman3',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'paintstore',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'django_mailman3.lib.auth.fedora',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.gitlab',
    #'allauth.socialaccount.providers.google',
)
