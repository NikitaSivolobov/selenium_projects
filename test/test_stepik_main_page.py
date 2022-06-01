from selenium_projects.pages.main_stepik_page import MainPage
from selenium_projects.pages.login_stepik_page import LoginPage
from selenium_projects.pages.dunlop_page import DunlopPage
# import time

# обновили функцию из задания
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаём в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    # time.sleep(10)


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    # time.sleep(10)


def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    # time.sleep(10)


def test_guest_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    # time.sleep(10)


def test_guest_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    # time.sleep(10)


def test_yngwie_malmsteen_1_5_pick(browser):
    link = "https://www.jimdunlop.com/"
    page = DunlopPage(browser, link)
    page.open()
    page.go_to_malmsteen_picks()
    # time.sleep(10)

if __name__ == '__main__':
    pytest.main()