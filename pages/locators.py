from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Селектор для ссылки перехода на форму логина

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # Селектор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Селектор для формы регистрации