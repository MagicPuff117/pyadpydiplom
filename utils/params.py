from config import FIELDS


def ask_params():
    user_id = input('Введите ваш id: ')
    age_from = input('Возраст не меньше: ')
    age_to = input('Возвраст не больше: ')
    sex = input('Пол (1 — Женский, 2 - Мужской, 0 - Нет привязки к полу): ')
    return user_id, sex, age_from, age_to


def ask_missing_params(user):
    updated_data = dict()
    for item in FIELDS.split(', ')[1:3]:
        if item not in user.user_data:
            updated_data[item] = input(f'{item.capitalize()} ID: ')
    for item in FIELDS.split(', ')[4:]:
        if item not in user.user_data or user.user_data[item] == '':
            if item == 'tv':
                updated_data[item] = input(f'Ваши любимые {item} шоу: ')
            else:
                updated_data[item] = input(f'Введите ваши {item}: ')
    return updated_data


def update_params(user):
    missing_params = ask_missing_params(user)
    if missing_params:
        user.update_user_data(missing_params)
