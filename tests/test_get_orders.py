import requests
import allure
from conftest import create_user
from helpers.constants import Urls, ErrorMessages, OrderData


class TestGetOrder:
    @allure.title('Проверка получения статуса заказа авторизованным пользователем')
    @allure.description('Регистрируем и авторизуем пользователя, делаем заказ и получаем информацию о заказе')
    def test_get_orders_by_authorized_user(self, create_user):
        # Берем из ответа сервера токен
        token = create_user[1].json()['accessToken']
        # Подготавливаем хэдеры для авторизации
        headers = {'Authorization': token}
        # Делаем запрос на создание заказа с корректным списком ингредиентов бургера и авторизацией
        response_create_order = requests.post(Urls.GET_ORDERS, headers=headers, data=OrderData.good_hash_order)
        # Делаем запрос на получение данных заказа
        response_get_order = requests.get(Urls.GET_ORDERS, headers=headers)
        # Проверяем, что статус ответа 200 и ответы при создании заказа и при получении информации о заказе - идентичны
        assert response_get_order.status_code == 200
        assert response_create_order.json()['order']['number'] == response_get_order.json()['orders'][0]['number']

    @allure.title('Проверка получения статуса заказа неавторизованным пользователем')
    @allure.description('Получаем информацию о заказе без авторизации, убеждаемся, что появляется ошибка ')
    def test_get_orders_by_unauthorized_user(self):
        # Отправляем запрос на получение информации о заказе не указывая токен авторизации
        response_get_orders = requests.get(Urls.GET_ORDERS)
        # Проверяем, что статус ответа НЕ успешен и есть сообщение You should be authorised в ответе на запрос
        assert response_get_orders.status_code == 401
        assert ErrorMessages.ORDER_NO_AUTH in response_get_orders.text
