API_URL = 'https://api.vk.com/method/users.get?'
VERSION = 5.21
TOKEN = input('Введите ваш токен: ')
FIELDS = 'sex, city, age, relation'
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7279354,
    'display': 'page',
    'scope': 'offline',
    'response_type': 'token'
}