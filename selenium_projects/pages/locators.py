from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class JimDunlopLocators():
    PRODUCTS_MENU = (By.XPATH, '//*[@id="expandibleHeader"]/a')
    VIEW_MORE_GUITAR_PICKS = ((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div/a/span'))
    VIEW_MORE_ARTIST_SERIES = (By.XPATH, '/html/body/div[3]/div[2]/div/div[15]/div[1]/div/a/span')
    YNGWIE_MALMSTEEN_1_5 = (By.XPATH, '//*[@id="product-listing-container"]/form/ul/li[1]/article/div/h4/a')
    TITLE_YNGWIE_MALMSTEEN = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div[1]/section[2]/div/div/h1")

class YandexLocators():
    SEARCH_FIELD = (By.CLASS_NAME, 'input__control')
    HINT_FIELD = (By.CLASS_NAME, 'mini-suggest__popup')
    SEARCH_RESULTS_ALL = (By.CSS_SELECTOR, 'serp-list')
    SEARCH_RESULTS_NUM = 'tensor.ru'



