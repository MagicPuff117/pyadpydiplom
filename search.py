from vkclass import VKUser
from score.scoring import score_users
from utils.params import ask_params, update_params
from db.writer import writer
from db.offset import get_offset, update_offset
from errors import *
import time


def get_top_matches(users):
    users_scores = dict()
    for user in users:
        users_scores[user] = user.score
    users_scores_sorted = sorted(users_scores.items(), key=lambda x: x[1], reverse=True)
    users_scores_list = users_scores_sorted[:10]
    return users_scores_list


def get_top_photos(photos_list):
    profile_photos = dict()
    for photo in photos_list:
        profile_photos[photo['id']] = [photo['likes']['count'], photo['sizes'][-1]['url']]
    profile_photos_sorted = sorted(profile_photos.items(), key=lambda x: x[1][0], reverse=True)
    profile_photos_list = profile_photos_sorted[:3]
    profile_photos_ids = dict()
    for photo in profile_photos_list:
        profile_photos_ids[str(photo[0])] = photo[1][1]
    return profile_photos_ids


@writer
def prepare_result(top_matches):
    result = list()
    for match in top_matches:
        photos_list = match[0].get_photos()
        top_photos = get_top_photos(photos_list)
        match_dict = {
            'id': str(match[0].user_id),
            'url': f'http://vk.com/id{match[0].user_id}',
            'photos': top_photos
        }
        result.append(match_dict)
        time.sleep(0.35)
    return result


def print_result(prepared_result):
    position = 1
    for match in prepared_result:
        print(f'{position}. Ссылка на профиль: {match["url"]}')
        for photo in match['photos'].values():
            print(f'Фото: {photo}')
        position += 1


def get_search_result():
    user_id, sex, age_from, age_to = ask_params()
    user = VKUser(user_id)
    user.get_user_data()
    if user.error == token_error:
        print('Неправильный токен, попробуйте еще раз')
    elif user.error == user_ban_del_error:
        print('Пользователь удален или забанен')
    elif user.error == user_existance:
        print('Пользователь не существует')
    else:
        update_params(user)
        print(f'Поиск по совпадениям по id {user.user_id}')
        offset = get_offset()
        search_results = user.search_users(sex, age_from, age_to, offset)[1]
        update_offset(offset)
        print('Scoring users')
        score_users(user, search_results)
        print('Получение топ совпадений')
        top_matches = get_top_matches(search_results)
        print('Подготвливаем результат')
        result = prepare_result(top_matches)
        print('Сохраняем в базу данных')
        print('Успешно завершено')
        print_result(result)
