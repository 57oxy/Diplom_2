import pytest
import allure
import requests
from conftest import create_user
from helpers.helpers import Credentials
from helpers.constants import Urls, ErrorMessages


class TestCreateUser:
    @allure.title('Проверка уникального пользователя')
    @allure.description('Отправляем запрос, проверяем успешный ответ')
    def test_create_user(self, create_user):
        # Получаем из фикстуры информацию о созданном пользователе и пишем в переменную
        response = create_user
        # Проверяем, что статус ответа 200 и в ответе есть 'success'
        assert response[1].status_code == 200
        assert response[1].json().get("success") is True


    @allure.title('Проверка повторной регистрации того же пользователя')
    @allure.description('Дважды отправляем запрос на создание пользователя, проверяем, что во второй раз ответ не 200')
    def test_create_exists_user(self, create_user):
        # Получаем из фикстуры информацию о созданном пользователе и пишем в переменную
        response = create_user
        # Готовим почву для второго запроса - олучаем логин и пароль из фикстуры, записываем
        payload = response[0]
        # Отправляем повторный запрос на создание пользователя с теми же данными
        response_exists_user = requests.post(Urls.CREATE_USER, data=payload)
        # Проверяем, что повторный запрос НЕ успешен - ошибка 403 с сообщением User already exists
        assert response_exists_user.status_code == 403
        assert response_exists_user.json().get('message') == ErrorMessages.USER_EXISTS

    @allure.title('Проверка регистрации пользователя с отсутствующими пользовательскими данными ')
    @allure.description('Отправляем через параметризацию запросы с данными без имейла, пароля, без имени, проверяем, что регистрация неуспешна')
    @pytest.mark.parametrize('data', [
        Credentials.create_user_data_without_email(),
        Credentials.create_user_data_without_password(),
        Credentials.create_user_data_without_name()
    ])
    def test_create_incorrect_user_data(self, data):
        # Отправляем запрос тело запроса указываем в параметризации некорректные варианты данных для регистрации
        response = requests.post(Urls.CREATE_USER, data=data)
        # Проверяем, что статус НЕ успешен - ошибка 403 и нет сообщения 'success'
        assert response.status_code == 403
        assert response.json().get("success") is False
