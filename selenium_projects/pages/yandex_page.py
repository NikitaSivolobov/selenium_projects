from .base_page import BasePage
from .locators import YandexLocators


class YandexPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*YandexLocators.SEARCH_FIELD), "Поле поиска не появилось"

    def tensor_search(self):
        link = self.browser.find_element(*YandexLocators.SEARCH_RESULTS)
        link.click()
        
        link = self.browser.find_element(*JimDunlopLocators.VIEW_MORE_GUITAR_PICKS)
        link.click()
        self.browser.execute_script("window.scrollBy(0, 7600);")

        link = self.browser.find_element(*JimDunlopLocators.VIEW_MORE_ARTIST_SERIES)
        link.click()
        self.browser.execute_script("window.scrollBy(0, 600);")

        link = self.browser.find_element(*JimDunlopLocators.YNGWIE_MALMSTEEN_1_5)
        link.click()

        text_el = self.browser.find_element(*JimDunlopLocators.TITLE_YNGWIE_MALMSTEEN)
        text = text_el.text

        assert "YNGWIE MALMSTEEN 1.52MM" == text, f"Нужный медиатор не выбран"