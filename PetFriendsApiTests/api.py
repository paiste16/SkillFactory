import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email: str, password: str) -> json:
        """Метод обращается через API к серверу, получает в ответ статус и результат в формате JSON в котором содержится
        ключ пользователя, который получен по паролю и email"""

        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: str, filter: str) -> json:
        """Метод обращается по API к серверу и возвращает статус запроса и ответ в формате JSON, который содержит список
        питомцем в соответствии с заявленным фильтром. Фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pets(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Метод отправляет по API данные для добавления нового питомца, в ответ статус и данные
        нового питомца в формате JSON"""

        data = MultipartEncoder (
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:

        """Метод отправляет DELETE-запрос на сервер и удаляет питомца по pet_id, который мы получаем из теста"""
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url+'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        """Метод меняет данные в последнем питомце на новые, которые мы получаем из теста, через PUT-запрос по pet_id, который мы тоже получаем из теста"""

        headers = {'auth_key': auth_key['key']}
        data = {'name': name,
                'age': age,
                'animal_type': animal_type}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result







