import pytest
import requests
from helpers.helpers import Credentials
from helpers.constants import Urls

# Фикстура сооздания пользователя
@pytest.fixture
def create_user():
    # Готовим логин пароль и имя для создания пользователя
    payload = Credentials.create_correct_user_data()
    # Отправляем запрос с данными пользователя и записываем ответ
    response = requests.post(Urls.CREATE_USER, data=payload)
    # Передаем данные пользователя и ответ после создания в тесты
    yield payload, response
    # Берем из ответа сервера токен
    token = response.json()['accessToken']
    # Отправляем запрос на удаление созданного пользователя
    requests.delete(Urls.UPDATE_USER, headers={"Authorization": token})
