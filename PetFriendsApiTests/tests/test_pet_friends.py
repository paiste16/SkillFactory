from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем, что логин и пароль валидны"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """Проверяем, что при валидном авторизационном ключе, полученном при авторизации, мы можем вызвать список всх питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pets_with_valid_data(name='Животный', animal_type='Крот', age='500', pet_photo='images/P1040103.jpg'):
    """Проверяем, что можно добавить нового питомца по-средством POST-запроса с валидными передаваемыми данными"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_pets_with_valid_pet_id():
    """Проверяем возможность удаления питомца из списка my_pets, при отсутствии таковых сначала добавляем нового питомца,
    а потом удаляем его через DELETE-запрос"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.add_new_pets(auth_key, 'Samsa', 'kaban', '333', 'images/cat1.jpeg')
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_pet_info(name='Zhuk', animal_type='diver', age=7):
    """Проверяем возможность внесения изменений в данные последнего питомца по-средством PUT-запроса с валидными данными,
    в случае отсутствия питомцев в my_pets вызываем исключение"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception('There is no my pets')


"""Далее мои негативные тесты"""

def test_get_api_key_for_not_valid_user(email=0, password=valid_password):
    """Проверяем, вернет ли сервер ключ авторизации при не валидном email"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_not_valid_password(email=valid_email, password=0):
    """Проверяем, вернет ли сервер ключ авторизации при не валидном пароле"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_my_pets_with_not_valid_filter(filter='my_pats'):
    """Проверяем, можем ли мы при валидном авторизационном ключе, полученном при авторизации,
    и не валидном фильтре получить список питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_get_my_pets_without_key(filter='my_pets'):
    """Проверяем, можем ли мы при валидном фильтре и без авторизационного ключа получить список моих питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(filter)
    assert status == 200
    assert len(result['pets']) > 0



def test_add_new_pets_with_not_valid_data(name=None, animal_type='Крот', age='500', pet_photo='images/P1040103.jpg'):
    """Проверяем, можно ли  добавить нового питомца по-средством POST-запроса с отсутствующими данными для поля name"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name



def test_add_new_pets_with_valid_data_and_name_equal_animal_type(name='Животный', animal_type='Крот', age='500', pet_photo='images/P1040103.jpg'):
    """Проверяем, что при валидных данных нового питомца в ответе имя может совпадать с типом животного"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == animal_type


def test_delete_pets_from_common_list(filter=''):
    """Проверяем, можно ли удалить питомца из общего списка"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    if len(my_pets['pets']) == 0:
        pf.add_new_pets(auth_key, 'Samsa', 'kaban', '333', 'images/cat1.jpeg')
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert pet_id not in my_pets.values()

    """Оказалось что можно и тест проходит, чужие зверюшки удаляются.... 
    но по идее не должен ведь!!!, но ведь тест реализован и мне кажется как вполне негативный)))"""



def test_delete_pets_without_auth_key():
    """Проверяем, будет ли удален питомец, если в запросе не передать авторизационный ключ"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.add_new_pets(auth_key, 'Samsa', 'kaban', '333', 'images/cat1.jpeg')
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()



def test_unsuccessful_update_pet_info_with_wrong_data_type(name='Zhuk', animal_type='diver', age='u'):
    """Метод update_pet_info принимает возраст как целое число. попробуем отправить ему строку"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception('There is no my pets')

    """Прокатывает, тест проходит и на сайте возраст меняется на u.... странно))))"""


def test_unsuccessful_update_pet_info_for_not_exist_pet(name='Zhuk', animal_type='diver', age=3):
    """Пробуем обновить данные питомца, которого нет в списке, запросим его по номеру,
    который значительно больше количества моих питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][55]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception('There is no my pets')








