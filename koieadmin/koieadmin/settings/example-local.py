# Secret key
SECRET_KEY = 'SUPER SECRET KEY' 

# If we should show debug. NO in prod!
DEBUG = False

TEMPLATE_DEBUG = False

# Allowed referers
ALLOWED_HOSTS = ['127.0.0.1', 'your.webpage.tld']

# Admins get notified about site crashes
ADMINS = (
	('Admin', 'admin@example.org'),
)

# Base url of webpage
BASE_URL = '127.0.0.1:8000'

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.db'),
    }
}

# Celery broker
BROKER_URL = 'amqp://guest:guest@localhost:5672'

# Email info
EMAIL_USE_TLS = True
EMAIL_HOST = 'email_server'
EMAIL_PORT = 0
EMAIL_HOST_USER = 'noreply@example.org'
EMAIL_HOST_PASSWORD = 'yourpassword'
