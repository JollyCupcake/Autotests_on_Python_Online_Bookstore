from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert "login" in self.browser.current_url, "Not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.email_registration = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        self.email_registration.send_keys(email)
        password = "FakePassword$55"
        self.password_registration = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        self.password_registration.send_keys(password)
        self.password_confirmation = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        self.password_confirmation.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


        