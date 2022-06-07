import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import YandexLocators


class YandexPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*YandexLocators.SEARCH_FIELD), "Поле поиска не появилось"
        print(f"Поле поиска присутствует на странице ====> УСПЕX!!!")

    def should_be_images_link(self):
        link = self.browser.find_element(*YandexLocators.IMAGES_LINK)
        assert self.is_element_present(*YandexLocators.IMAGES_LINK), 'Ссылка "Картинки" отсутствует на странице'
        print(f"Ссылка <<{link.text}>> присутствует на странице ====> УСПЕX!!!")

    def should_be_images_url(self):
        self.browser.find_element(*YandexLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert YandexLocators.IMAGES_URL in self.browser.current_url, "Images is not presented in URL"
        print(f"Мы переходим на url {YandexLocators.IMAGES_URL} ====> УСПЕШНО!!!")

    def should_be_tensor_search(self):
        self.browser.find_element(*YandexLocators.SEARCH_FIELD).send_keys("тензор")
        assert self.is_element_present(*YandexLocators.HINT_FIELD), "Таблица с подсказками (suggest) не появилась"

    def tensor_search(self):
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

    def should_be_images_equal(self):
        self.browser.find_element(*YandexLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        first_category = self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).text
        self.browser.find_element(*YandexLocators.IMAGES_FIRST_CATEGORY).click()
        time.sleep(1)

        assert first_category in self.browser.title, f"{first_category} is not presented in URL"

        print(f"Мы переходим на 1 категорию {first_category} ====> УСПЕШНО!!!")

        # self.browser.find_element(*YandexLocators.IMAGES_TEXT_FIRST_CATEGORY).send_keys(
        #     Keys.CONTROL + "a")
        # self.browser.find_element(*YandexLocators.IMAGES_TEXT_FIRST_CATEGORY).\
        #     send_keys(Keys.CONTROL + "c")
        #
        # text_search_field.send_keys(Keys.CONTROL + "v")
        # print(text_search_field)
        #
        # time.sleep(3)
        #text_search_field = self.browser.find_element(*YandexLocators.IMAGES_TEXT_FIRST_CATEGORY).click().send_keys(Keys.CONTROL + "a").send_keys(Keys.CONTROL + "c")
        #text_search_field = self.browser.find_element(*YandexLocators.IMAGES_TEXT_FIRST_CATEGORY).send_keys(Keys.CONTROL + "a").send_keys(Keys.CONTROL + "c")
        #print(text_search_field)

        # assert YandexLocators.IMAGES_URL in self.browser.current_url, "Images is not presented in URL"
        # print()
        # print(f"Мы переходим на url {YandexLocators.IMAGES_URL} ====> УСПЕШНО!!!")


