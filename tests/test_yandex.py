from selenium_projects.pages.yandex_page import YandexPage
import time


def test_search_field(browser):
    link = "https://www.yandex.com/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_search_field()
    time.sleep(5)

if __name__ == '__main__':
    pytest.main()