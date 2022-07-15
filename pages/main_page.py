from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators

class MainPage(BasePage): 
    def should_be_cart_lint(self):
        assert self.is_element_present(*CartPageLocators.CART_LINK), "Cart didn't found"
