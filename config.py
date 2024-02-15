from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

#Website Credentials
API_KEY = environ.get('API_KEY', '45934131f969873f53398f12641137fd967eaa84')
API_URL = environ.get('API_URL', 'https://showtimelinks.com/api')
WEB_NAME = environ.get('WEB_NAME', 'ShowtimeLinks')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/pandaztalks')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/pandaznetwork')
