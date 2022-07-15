from pages.main_page import MainPage
import time


def test_button_add_to_basket_is_visible(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
    time.sleep(5)
        
    page.should_be_cart_lint()