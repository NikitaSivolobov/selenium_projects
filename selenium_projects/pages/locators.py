from selenium.webdriver.common.by import By


class MainPageLocators():
    # Тестирование главной страницы с задания урока Stepik
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Тестирование страницы с задания урока Stepik
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class JimDunlopLocators():
    # Тестирование медиатора Malmsteen на сайте Jim Dunlop
    PRODUCTS_MENU = (By.XPATH, '//*[@id="expandibleHeader"]/a')
    VIEW_MORE_GUITAR_PICKS = ((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div/a/span'))
    VIEW_MORE_ARTIST_SERIES = (By.XPATH, '/html/body/div[3]/div[2]/div/div[15]/div[1]/div/a/span')
    YNGWIE_MALMSTEEN_1_5 = (By.XPATH, '//*[@id="product-listing-container"]/form/ul/li[1]/article/div/h4/a')
    TITLE_YNGWIE_MALMSTEEN = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div[1]/section[2]/div/div/h1")

class YandexLocators():
    # Тестирование Тензор в Яндексе
    SEARCH_FIELD = (By.CLASS_NAME, 'input__control')
    HINT_FIELD = (By.CLASS_NAME, 'mini-suggest__popup')
    SEARCH_RESULTS_ALL = (By.CSS_SELECTOR, 'serp-list')
    SEARCH_RESULT_NUM = (By.XPATH, '//div[@class="VanillaReact OrganicTitle OrganicTitle_wrap Typo Typo_text_l Typo_line_m organic__title-wrapper"]/a')
    SEARCH_START = 0
    SEARCH_LAST = 5
    SEARCH_RESULT = 'tensor.ru'

    # Тестирование "Картинок" в Яндексе
    IMAGES_LINK = (By.XPATH, '//a[@data-id="images"]/div[@class="services-new__item-title"]')
    IMAGES_URL = 'https://yandex.ru/images/'
    IMAGES_FIRST_CATEGORY = (By.XPATH, "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']")
    IMAGES_ALL_FIRST = (By.CSS_SELECTOR, "div.serp-item__preview")

    BUTTON_PREV0 = (By.XPATH, "CircleButton CircleButton_disabled")
    BUTTON_NEXT = (By.XPATH, "//div[contains(@class, 'CircleButton_type_next')]")
    BUTTON_PREV1 = (By.XPATH, "//div[contains(@class, 'CircleButton_type_prev')]")

    IMAGE_FIRST = (By.CSS_SELECTOR, "img.MMImage-Origin")
    IMAGE_SECOND = (By.CSS_SELECTOR, "img.MMImage-Origin")
    IMAGE_BACK = (By.CSS_SELECTOR, "img.MMImage-Origin")





