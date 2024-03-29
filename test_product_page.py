from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link) # инициализируем Page Object ProductPage
    product_page.open()                       
    product_page.add_product_to_basket()  # вызываем метод добавления товара в корзину
    product_page.solve_quiz_and_get_code() #вызываем метод расчёта
    time.sleep(5)
    assert product_page.get_product_name() == product_page.get_added_product_name(), "Product added name is not equal to the product original name"
    assert product_page.get_product_price() == product_page.get_added_product_price(), "Basket price is not equal to the product original price"


