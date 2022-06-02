import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


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
        result_links = self.browser.find_elements(By.XPATH, '//div[@class="VanillaReact OrganicTitle OrganicTitle_wrap Typo Typo_text_l Typo_line_m organic__title-wrapper"]/a')

        list_link = []
        for element in result_links:
            item_link = element.get_attribute('href')
            list_link.append(item_link)
        print()
        print(*list_link[:5], sep="\n")

        # assert self.browser.find_element(*YandexLocators.SEARCH_RESULTS_NUM), 'tensor.ru отсутствует'
