from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv('JWT_SECRET_KEY', None)

MAIL_SERVER = getenv('MAIL_SERVER', None)
MAIL_PORT = getenv('MAIL_PORT', None)
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = getenv('MAIL_USERNAME', None)
MAIL_PASSWORD = getenv('MAIL_PASSWORD', None)

ADMINS = ['bramburkamu@gmail.com']