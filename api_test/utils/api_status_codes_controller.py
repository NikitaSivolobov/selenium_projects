from api_test.utils.http_methods import Http_methods


"""Методы для тестирования различных статус кодов для метода GET Api Status Codes Controller"""

base_url = "http://85.192.34.140:8080"           # Базовая URL


class Status_codes_controller():


    """Метод для проверки 400 кода ответа - Плохой запрос:
     клиент отправляет запрос с неполными данными, плохо построенными данными или недопустимыми данными"""

    @staticmethod
    def get_bad_request():

        get_resource = "/api/bad-request"  # Ресурс метода Get 400 bad-request
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 201 кода ответа - Создан: сервер подтвердил создание ресурса"""
    @staticmethod
    def get_created():
        get_resource = "/api/created"  # Ресурс метода Get 201 created
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 403 кода ответа - Запрещено: ресурс,
     к которому клиент пытается получить доступ, запрещен/нет прав"""

    @staticmethod
    def get_forbidden():
        get_resource = "/api/forbidden"  # Ресурс метода Get forbidden 403
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 404 кода ответа - Не найден: 
     сервер доступен, но конкретная страница, которую ищет клиент, не найдена/не существует."""

    @staticmethod
    def get_invalid_url():
        get_resource = "/api/invalid-url"  # Ресурс метода Get invalid-url 404
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 301 кода ответа - Перемещено навсегда: сервер сообщает клиенту,
     что искомый ресурс, был навсегда перемещен по другому URL-адресу.
    Все пользователи и боты будут перенаправлены на новый URL. """

    @staticmethod
    def get_moved():
        get_resource = "/api/moved"  # Ресурс метода Get 301
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 204 кода ответа - Не найден: сервер доступен, но конкретная страница,
     которую ищет клиент, не найдена/не существует"""

    @staticmethod
    def get_no_content():
        get_resource = "/api/no-content"  # Ресурс метода Get forbidden 204
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для проверки 401 кода ответа - Неавторизованый:
     для доступа клиента к запрошенному ресурсу требуется авторизация."""

    @staticmethod
    def get_unauthorized():
        get_resource = "/api/unauthorized"  # Ресурс метода Get forbidden 401
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get
