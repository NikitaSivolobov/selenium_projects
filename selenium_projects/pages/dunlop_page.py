from .base_page import BasePage
from .locators import JimDunlopLocators


class DunlopPage(BasePage):
    def go_to_malmsteen_picks(self):
        link = self.browser.find_element(*JimDunlopLocators.PRODUCTS_MENU)
        link.click()
        self.browser.execute_script("window.scrollBy(0, 800);")

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

        assert "YNGWIE MALMSTEEN 1.5MM" == text, f"Нужный медиатор не выбран"

        print("Тест на проверку наличия медиатора YNGWIE MALMSTEEN 1.5MM прошёл")
        print("======")
