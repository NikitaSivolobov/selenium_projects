import allure
import json

from requests import Response

from api_test.utils.checking import Checking
from api_test.utils.api_status_codes_controller import Status_codes_controller

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test Status Codes Controller")
class Test_status_codes_controller():

    @allure.description("Test GET Status Codes 400 Bad Request - Плохой запрос: "
                        "клиент отправляет запрос с неполными данными,"
                        " плохо построенными данными или недопустимыми данными")
    def test_bad_request(self):
        print()
        print("Метод GET Bad Request")
        result_get: Response = Status_codes_controller.get_bad_request()
        Checking.check_status_code(result_get, 400)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'statusCode', 400)
        Checking.check_json_value(result_get, 'description', 'Bad Request')

    @allure.description("Test GET Status Codes 201 Created - Создан: сервер подтвердил создание ресурса")
    def test_created(self):
        print()
        print("Метод GET Created")
        result_get: Response = Status_codes_controller.get_created()
        Checking.check_status_code(result_get, 201)
        Checking.check_json_token(result_get, ['statusCode', 'description'])
        Checking.check_json_value(result_get, 'statusCode', 201)
        Checking.check_json_value(result_get, 'description', 'created')


    @allure.description("Test GET Status Codes 403 Forbidden - Запрещено")
    def test_forbidden(self):
        print()
        print("Метод GET Forbidden")
        result_get: Response = Status_codes_controller.get_forbidden()
        Checking.check_status_code(result_get, 403)
        Checking.check_json_token(result_get, ['statusCode', 'description'])
        Checking.check_json_value(result_get, 'statusCode', 403)
        Checking.check_json_value(result_get, 'description', 'Forbidden')


    @allure.description("Test GET Status Codes 404  Не найден: "
                        "сервер доступен, но конкретная страница, которую ищет клиент, не найдена/не существует.")
    def test_invalid_url(self):
        print()
        print("Метод GET Not Found")
        result_get: Response = Status_codes_controller.get_invalid_url()
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['statusCode', 'description'])
        Checking.check_json_value(result_get, 'statusCode', 404)
        Checking.check_json_value(result_get, 'description', 'Not Found')


    @allure.description("Test GET Status Codes 301 кода ответа - Перемещено навсегда: сервер сообщает клиенту,"
                        "что искомый ресурс, был навсегда перемещен по другому URL-адресу."
                        "Все пользователи и боты будут перенаправлены на новый URL. ")
    def test_moved(self):
        print()
        print("Метод GET Moved Permanently")
        result_get: Response = Status_codes_controller.get_moved()
        Checking.check_status_code(result_get, 301)
        Checking.check_json_token(result_get, ['statusCode', 'description'])
        Checking.check_json_value(result_get, 'statusCode', 301)
        Checking.check_json_value(result_get, 'description', 'Moved Permanently')


    @allure.description("Test GET Status Codes 204 Не найден: сервер доступен, но конкретная страница, "
                        "которую ищет клиент, не найдена/не существует")
    def test_no_content(self):
        print()
        print("Метод GET No content")
        result_get: Response = Status_codes_controller.get_no_content()
        Checking.check_status_code(result_get, 204)


    @allure.description("Test GET Status Codes 401 Неавторизованый: для доступа клиента к запрошенному ресурсу требуется авторизация.")
    def test_unauthorized(self):
        print()
        print("Метод GET Unauthorized")
        result_get: Response = Status_codes_controller.get_unauthorized()
        Checking.check_status_code(result_get, 401)
        Checking.check_json_token(result_get, ['timestamp', 'status', 'error', 'path'])
        Checking.check_json_search_word_in_value(result_get, 'timestamp', "2023-01-25T09")
        Checking.check_json_value(result_get, 'status', 401)
        Checking.check_json_value(result_get, 'error', 'Unauthorized')
        Checking.check_json_value(result_get, 'path', '/api/unauthorized')


