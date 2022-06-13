import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import YandexLocators


class YandexPage(BasePage):
    def should_be_search_field(self):
        """Поле поиска присутствует на главной странице Яндекса"""

        assert self.is_element_present(*YandexLocators.SEARCH_FIELD), "Поле поиска не появилось"
        print(f"Поле поиска присутствует на странице ====> УСПЕX!!!")

    def should_be_images_link(self):
        """Раздел "Картинки" присутствует на главной странице Яндекса"""

        link = self.browser.find_element(*YandexLocators.IMAGES_LINK)
        assert self.is_element_present(*YandexLocators.IMAGES_LINK), 'Ссылка "Картинки" отсутствует на странице'
        print(f"Ссылка <<{link.text}>> присутствует на странице ====> УСПЕX!!!")

    def should_be_images_url(self):
        """
            При переходе в раздел "Картинки" с главной страницы Яндекса
            в url содержится https://yandex.ru/images/
        """
        self.browser.find_element(*YandexLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert YandexLocators.IMAGES_URL in self.browser.current_url, "Images is not presented in URL"
        print(f"Мы переходим на url {YandexLocators.IMAGES_URL} ====> УСПЕШНО!!!")

    def should_be_tensor_search(self):
        """При вводе в поиск "тензор" появляется таблица с подсказками"""

        self.browser.find_element(*YandexLocators.SEARCH_FIELD).send_keys("тензор")
        assert self.is_element_present(*YandexLocators.HINT_FIELD), "Таблица с подсказками (suggest) не появилась"

    def tensor_search(self):
        """Проверка наличия tensor.ru в первых 5 результатах поиска (можно задавать любой диапазон поиска)"""
        self.browser.find_element(*YandexLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        result_links = self.browser.find_elements(*YandexLocators.SEARCH_RESULT_NUM)

        list_link = []
        for element in result_links:
            item_link = element.get_attribute('href')
            list_link.append(item_link)

        flag_results = False
        for link in list_link[YandexLocators.SEARCH_START:YandexLocators.SEARCH_LAST]:
            if YandexLocators.SEARCH_RESULT in link:
                flag_results = True
                break

        assert flag_results, f'{YandexLocators.SEARCH_RESULT} отсутствует'

        print(f"Тест на проверку наличия {YandexLocators.SEARCH_RESULT} в списке результатов поиска\nс "
        f"{str(YandexLocators.SEARCH_START+1)} по {str(YandexLocators.SEARCH_LAST)} ссылки прошёл ====> УСПЕШНО!!!")

        print()
        print("Ссылки c " + str(YandexLocators.SEARCH_START + 1) + " по " + str(YandexLocators.SEARCH_LAST) +
              " в списке результатов поиска:")
        print(*list_link[YandexLocators.SEARCH_START:YandexLocators.SEARCH_LAST], sep="\n")

    def should_be_images_first_category(self):
        """
            При переходе в 1 категорию картинок в разделе "Картинки" Яндекса,
            действительно открывается 1 категория
        """
        self.browser.find_element(*YandexLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        first_category = self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).text
        self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).click()
        time.sleep(1)

        assert first_category in self.browser.title, f"{first_category} is not presented in URL"

        print(f"Мы переходим на 1 категорию {first_category} ====> УСПЕШНО!!!")

    def should_be_images_equal(self):
        """
            При переходе в 1 категорию картинок в разделе "Картинки" Яндекса,
            1 открытая картинка совпадает после перехода на следующую картинку и возврата назад
        """
        self.browser.find_element(*YandexLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        first_category = self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).text
        print(f"Первая категория раздела <Картинки> ====> {first_category}")
        self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).click()
        self.browser.find_element(*YandexLocators.IMAGES_ALL_FIRST).click()
        image_first = self.browser.find_element(*YandexLocators.IMAGE_FIRST).get_attribute('src')
        print(f"Первое изображение: {image_first}")

        self.browser.find_element(*YandexLocators.BUTTON_NEXT).click()
        image_second = self.browser.find_element(*YandexLocators.IMAGE_SECOND).get_attribute('src')
        print(f"Следующее изображение: {image_second}")

        assert image_first != image_second, f"Первое и второе изображение категории: '{first_category}' равны"

        self.browser.find_element(*YandexLocators.BUTTON_PREV1).click()
        image_back = self.browser.find_element(*YandexLocators.IMAGE_BACK).get_attribute('src')
        print(f"Изображение после возврата: {image_back}")

        assert image_first == image_back, f"Изображения {first_category} не равны"

        print(f"Изображения {first_category} до перехода и после возврата равны, тест ====> УСПЕШЕН!!!")

