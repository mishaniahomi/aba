# DATABASES_setting = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',
#         'NAME': 'p306595_735',
#         'USER': 'root',
#         'PASSWORD': '1qaz!QAZ',
#         'HOST': 'localhost',
#         'PORT': '3306'
#     }
# }
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES_setting = {
    'default': {
        "ENGINE":"django.db.backends.mysql",
        "NAME": "db_django",
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "3306"),
    }
}
