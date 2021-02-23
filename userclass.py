import requests
from config import API_URL, VERSION, TOKEN, FIELDS
from urllib.parse import urlencode
from pprint import pprint

class VkUser():
    user_id = None
    # print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))
    def __init__(self, user_id):
        self.id = user_id
        self.user = {'access_token': TOKEN,
                     'user_ids': self.id,
                     'v': VERSION
                     }

        response_user = requests.get(API_URL, urlencode(self.user))
        user_info = response_user.json()
        pprint(user_info)



VkUser(17460386)