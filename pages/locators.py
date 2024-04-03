from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Ссылка перехода на форму логина

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # Форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Форма регистрации

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket") # Кнопка "Добавить в корзину"
    PRODUCT_NAME = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] h1") # Наименованин продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']") # Стоимость продукта
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong") # Наименование добавленного в корзину продукта
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-info  fade in'] strong") # Цена добавленного в корзину продукта
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)") # Сообщение об успешном добавлении продукта в корзину

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")