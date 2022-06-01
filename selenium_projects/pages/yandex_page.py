from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import YandexLocators


class YandexPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*YandexLocators.SEARCH_FIELD), "Поле поиска не появилось"

    def should_be_tensor_search(self):
        self.browser.find_element(*YandexLocators.SEARCH_FIELD).send_keys("тензор")
        assert self.is_element_present(*YandexLocators.HINT_FIELD), "Таблица с подсказками (suggest) не появилась"

    def tensor_search(self):
        self.browser.find_element(*YandexLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        assert self.browser.find_element(*YandexLocators.SEARCH_RESULTS_NUM), "tensor.ru отсутствует"
