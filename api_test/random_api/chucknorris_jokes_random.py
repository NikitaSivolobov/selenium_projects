import requests

class Test_new_joke():
    """Получение новой шутки про Чака Норриса"""

    def __init__(self):
        pass
    def test_get_new_random_joke(self):
        """Получение новой случайной шутки про Чака Норриса"""
        url = "https://api.chucknorris.io/jokes/random"

        result = requests.get(url)
        print("Status code ==> " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Тест успешно пройден, получена новая шутка!!")
        else:
            print("Тест не пройден :-(, FAILED!!")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck присутствует")
        else:
            print("Chuck отсутствует")


    def test_get_new_random_categories_joke(self):
        """Получение новой случайной шутки про Чака Норриса из категории Музыка """
        category = "music"
        url = "https://api.chucknorris.io/jokes/random?category=" + category

        result = requests.get(url)
        print("Status code ==> " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Тест успешно пройден, получена новая шутка!!")
        else:
            print("Тест не пройден :-(, FAILED!!")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["music"]
        print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck присутствует")
        else:
            print("Chuck отсутствует")


randome_joke = Test_new_joke()
randome_joke.test_get_new_random_joke()


music_joke = Test_new_joke()
music_joke.test_get_new_random_categories_joke()
