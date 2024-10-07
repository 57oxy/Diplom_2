from faker import Faker


class Credentials:

    # Создаем корректные данные пользователя
    @staticmethod
    def create_correct_user_data():
        # Создаем объект класса Фейкер
        faker = Faker()
        # Создаем словарь с данными пользователя и возвращаем его
        login_pass = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return login_pass

    # Создаем данные пользователя без email
    @staticmethod
    def create_user_data_without_email():
        # Создаем объект класса Фейкер
        faker = Faker()
        # Создаем словарь с данными пользователя и возвращаем его
        login_pass = {
            'password': faker.password(),
            'name': faker.first_name()
        }
        return login_pass

    # Создаем данные пользователя без имени
    @staticmethod
    def create_user_data_without_name():
        # Создаем объект класса Фейкер
        faker = Faker()
        # Создаем словарь с данными пользователя и возвращаем его
        login_pass = {
            'email': faker.email(),
            'password': faker.password()
        }
        return login_pass

    # Создаем данные пользователя без пароля
    @staticmethod
    def create_user_data_without_password():
        # Создаем объект класса Фейкер
        faker = Faker()
        # Создаем словарь с данными пользователя и возвращаем его
        login_pass = {
            'email': faker.email(),
            'name': faker.first_name()
        }
        return login_pass
