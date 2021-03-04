

API_URL = 'https://api.vk.com/method'
VERSION = '5.85'
TOKEN = input('Введите ваш токен: ')
FIELDS = 'sex, city, country, common_count, interests, music, movies, tv, books'


OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7279354,
    # 'redirect_uri':
    'display': 'page',
    'scope': 'offline',
    'response_type': 'token'
}