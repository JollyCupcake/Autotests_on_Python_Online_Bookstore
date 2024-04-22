from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Ссылка перехода на форму логина
    BASKET_LINK = (By.CSS_SELECTOR, "span .btn-default:nth-child(1)") # Кнопка перехода в корзину

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # Форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Форма регистрации
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email") # Email на форме регистрации
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1l") # Пароль на форме регистрации
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2") # Подтверждение пароля на форме регистрации
    REGISTER_BUTTON = (By.NAME, "registration_submit") # Кнопка Register

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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p") # Сообщение, что корзина пуста
    BASKET_CONTAINS_PRODUCTS = (By.CSS_SELECTOR, "[class='basket-items']") # Наименование блока, в котором отображаются добавленные товары