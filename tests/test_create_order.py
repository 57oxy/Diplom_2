import requests
import allure
from conftest import create_user
from helpers.constants import Urls, ErrorMessages, OrderData


class TestCreateOrder:

    @allure.title('Проверка создания заказа c ингредиентами авторизованным пользователем')
    @allure.description('Регистрируем и авторизуем пользователя, делаем заказ')
    def test_create_order_with_authorized_user_with_ingredients(self, create_user):
        # Берем из ответа сервера токен
        token = create_user[1].json()['accessToken']
        # Подготавливаем хэдеры для авторизации
        headers = {'Authorization': token}
        # Делаем запрос с корректными ингредиентами бургера
        response = requests.post(Urls.GET_ORDERS, headers=headers, data=OrderData.good_hash_order)
        # Проверяем что запрос успешен
        assert response.status_code == 200
        assert response.json().get('success') is True

    # БАГ!!! Неавторизованный пользователь может оформить заказ с номером 9999 должен отображаться статус ошибки 401
    @allure.title('Проверка, что неавторизованный пользователь не может создать заказ (БАГ!!!) должен отображаться статус ошибки 401')
    @allure.description('Отсылаем запрос на создание заказа без авторизации')
    def test_create_order_by_unauthorized_user(self):
        # Делаем запрос с корректными ингредиентами бургера без авторизации
        response = requests.post(Urls.GET_ORDERS, data=OrderData.good_hash_order)
        # Проверяем что запрос НЕ успешен (БАГ) - запрос проходит успешно
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Проверка, что авторизованный пользователь не может сделать заказ передав некорректные хеши ингридиентов')
    @allure.description('Регистрируем пользователя, авторизованный пользователь пытается создать заказ с отсутствующими ингредиентами')
    def test_create_order_with_invalid_ingredients(self, create_user):
        # Берем из ответа сервера токен
        token = create_user[1].json()['accessToken']
        # Подготавливаем хэдеры для авторизации
        headers = {'Authorization': token}
        # Делаем запрос с некорректными ингредиентами бургера
        response = requests.post(Urls.GET_ORDERS, headers=headers, data=OrderData.wrong_hash_order)
        # Проверяем что запрос НЕ успешен - ответ 500
        assert response.status_code == 500
        assert ErrorMessages.INTERNAL_SERVER_ERROR in response.text

    @allure.title('Проверка что нельзя сделать заказ без ингредиентов')
    @allure.description('Регистрируем пользователя, авторизованный пользователь пытается создать заказ')
    def test_create_order_without_ingredients(self, create_user):
        # Берем из ответа сервера токен
        token = create_user[1].json()['accessToken']
        # Подготавливаем хэдеры для авторизации
        headers = {'Authorization': token}
        # Делаем запрос с пустым списком ингредиентов бургера
        response = requests.post(Urls.GET_ORDERS, headers=headers, data=OrderData.empty_ingredients)
        # Проверяем что запрос НЕ успешен - ответ 400
        assert response.status_code == 400
        assert response.json().get('success') is False
