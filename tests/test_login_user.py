import allure
import requests
from conftest import create_user
from helpers.helpers import Credentials
from helpers.constants import Urls


class TestLoginUser:
    @allure.title('Проверка вход в аккаунт зарегистрированного пользователя')
    @allure.description('Создаем корректного пользователя, логиним его в систему, затем удаляем пользователя')
    def test_correct_login_user(self, create_user):
        # Получаем из фикстуры информацию о созданном пользователе и пишем в переменную
        response = create_user
        # Отправляем запрос на вход в аккаунт с учетными данными зарегистрированного пользователя
        login = requests.post(Urls.LOGIN_USER, data=response[0])
        # Проверяем, что статус ответа успешный и есть 'success' в ответе
        assert login.status_code == 200
        assert login.json().get("success") is True

    @allure.title('Проверка логина не зарегистрированного пользователя')
    @allure.description('Логиним пользователя без регистрации, затем удаляем пользователя')
    def test_login_user_notexists(self):
        # Отправляем запрос на вход в аккаунт с учетными данными не зарегистрированного пользователя (с некорректными данными))
        login = requests.post(Urls.LOGIN_USER, data=Credentials.create_user_data_without_name())
        # Проверяем, что ответ НЕ успешен - ошибка 401 пользователь не авторизован
        assert login.status_code == 401
        assert login.json().get("success") is False
