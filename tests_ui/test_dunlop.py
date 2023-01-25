from selenium_projects.pages.dunlop_page import DunlopPage
import time


def test_yngwie_malmsteen_1_5_pick(browser):
    link = "https://www.jimdunlop.com/"
    page = DunlopPage(browser, link)
    page.open()
    page.go_to_malmsteen_picks()


if __name__ == '__main__':
    pytest.main()