from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
    
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
    
    def get_added_product_name(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        return added_product_name
    
    def get_added_product_price(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        return added_product_price
    
    def should_not_be_success_message_element_not_present(self): # Проверяет, что элемент не отображается
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_element_disappeared(self): # Проверяет, что элемент отображается, но затем исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

