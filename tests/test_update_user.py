import pytest
import requests
import allure
from conftest import create_user
from helpers.helpers import Credentials
from helpers.constants import Urls, ErrorMessages


class TestChangeUserData:

    @allure.title('Проверка изменения пользовательских данных')
    @allure.description('Создаем пользователя, изменяем данные пользователя, проверяем, что приходит корректный ответ, удаляем пользователя')
    @pytest.mark.parametrize('data', [
        Credentials.create_correct_user_data()['name'],
        Credentials.create_correct_user_data()['email'],
        Credentials.create_correct_user_data()['password']
    ])
    def test_change_authorized_user_data(self, create_user, data):
        # Берем из ответа сервера токен
        token = create_user[1].json()['accessToken']
        # Подготавливаем хэдеры для авторизации
        headers = {'Authorization': token}
        # Делаем запрос на обновление данных авторизованного пользователя, в параметрах указываем разные данные для изменения
        response = requests.patch(Urls.UPDATE_USER, headers=headers, data=data)
        # Проверяем, что статус запроса на изменение данных - успешный
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Проверка, что данные пользователя не изменить без авторизации')
    @allure.description('Отсылаем запрос на изменение данных пользователя, проверяем, что запрос не успешен')
    @pytest.mark.parametrize('data', [
        Credentials.create_correct_user_data()['name'],
        Credentials.create_correct_user_data()['email'],
        Credentials.create_correct_user_data()['password']
    ])
    def test_change_unauthorized_user_data(self, data):
        # Делаем запрос на обновление данных без авторизации, в параметрах указываем разные данные для изменения
        response = requests.patch(Urls.UPDATE_USER, data=data)
        # Проверяем, что код ответа 401 и в сообщении есть You should be authorised
        assert response.status_code == 401
        assert response.json().get('message') == ErrorMessages.UPDATE_NO_AUTH
