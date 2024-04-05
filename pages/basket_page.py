from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_that_basket_empty(self): # Проверяем наличие текста о том, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "No message that the basket is empty"

    def basket_is_empty(self): # Проверяем, что в корзине нет добавленных товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_PRODUCTS), "Basket is not empty, but should be"