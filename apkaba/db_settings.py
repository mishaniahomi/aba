DATABASES_setting = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
# import os
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
#
# DATABASES_setting = {
#     'default': {
#         "ENGINE":"django.db.backends.mysql",
#         "NAME": "db_django",
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "db"),
#         "PORT": os.environ.get("SQL_PORT", "3306"),
#     }
# }
