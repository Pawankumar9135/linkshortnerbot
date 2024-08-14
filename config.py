from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', '21993132'))
API_HASH = environ.get('API_HASH', '64adb3f672a2c32d71b447903c4b3476')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

#Website Credentials
API_KEY = environ.get('API_KEY', 'fb1686fb8d9c9040413748ad714b1bafbaf0533d')
API_URL = environ.get('API_URL', 'https://publicearn.com/api')
WEB_NAME = environ.get('WEB_NAME', 'publicearn')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/pj_central')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/pj_central')
