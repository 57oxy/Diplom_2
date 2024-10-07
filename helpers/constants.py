#  Ссылки на ручки API
class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    UPDATE_USER = f"{BASE_URL}/api/auth/user"
    GET_ORDERS = f"{BASE_URL}/api/orders"

# Тексты сообщений об ошибке
class ErrorMessages:
    USER_EXISTS = "User already exists"
    UPDATE_NO_AUTH = "You should be authorised"
    ORDER_NO_AUTH = "You should be authorised"
    INTERNAL_SERVER_ERROR = 'Internal Server Error'

# Ингредиенты в заказах
class OrderData:
    good_hash_order = {"ingredients":  ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"]}
    wrong_hash_order = {"ingredients":  ["aa1234", "bb12345", "cc1233"]}
    empty_ingredients = {"ingredients": []}
