import sys
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if 'test' in sys.argv:
    DB_PROPS = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    DBG = True
else:
    DB_PROPS = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'transya',
            'USER': 'root',
            'PASSWORD': 'backtrack5',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {'charset': 'utf8mb4'},
            # 'OPTIONS': {
            #     'read_default_file': '/etc/my.cnf',
            # }
        }
    }
    DBG = True


PROTOCOL = 'http'
DOMAIN = 'localhost'

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
EXPORT_PATH = os.path.join(PROJECT_ROOT, 'static/taskrobot/export/')
