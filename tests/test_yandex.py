import pytest

from selenium_projects.pages.yandex_page import YandexPage
import time


def test_search_field(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_search_field()

def test_tensor_search(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_search_field()
    page.should_be_tensor_search()
    page.tensor_search()

def test_yandex_images_link(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_images_link()

def test_yandex_images_url(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_images_url()

def test_yandex_images_first_category(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_images_first_category()

def test_yandex_images_first_second_back(browser):
    link = "https://www.yandex.ru/"
    page = YandexPage(browser, link)
    page.open()
    page.should_be_images_equal()

if __name__ == '__main__':
    pytest.main()