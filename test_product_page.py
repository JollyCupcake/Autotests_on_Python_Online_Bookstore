from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.parametrize('promocode', ["?promo=offer0",
                                       "?promo=offer1",
                                       "?promo=offer2",
                                       "?promo=offer3",
                                       "?promo=offer4",
                                       "?promo=offer5",
                                       "?promo=offer6",
                                       pytest.param("?promo=offer7", marks=pytest.mark.xfail), 
                                       "?promo=offer8",
                                       "?promo=offer9"])
                                       
def test_guest_can_add_product_to_basket(browser, promocode):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promocode}"
    product_page = ProductPage(browser, link) # инициализируем Page Object ProductPage
    product_page.open()                       
    product_page.add_product_to_basket()  # вызываем метод добавления товара в корзину
    product_page.solve_quiz_and_get_code() #вызываем метод расчёта
    time.sleep(5)
    assert product_page.get_product_name() == product_page.get_added_product_name(), "Product added name is not equal to the product original name"
    assert product_page.get_product_price() == product_page.get_added_product_price(), "Basket price is not equal to the product original price"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link) # инициализируем Page Object ProductPage
    product_page.open()                       
    product_page.add_product_to_basket()  # вызываем метод добавления товара в корзину
    product_page.solve_quiz_and_get_code() #вызываем метод расчёта
    # time.sleep(5)
    product_page.should_not_be_success_message_element_not_present() 

def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link) # инициализируем Page Object ProductPage
    product_page.open()                       
    product_page.should_not_be_success_message_element_not_present() 
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link) # инициализируем Page Object ProductPage
    product_page.open()                       
    product_page.add_product_to_basket()  # вызываем метод добавления товара в корзину
    product_page.solve_quiz_and_get_code() #вызываем метод расчёта
    # time.sleep(1)
    product_page.should_not_be_success_message_element_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page() #переход на страницу корзины
    basket_page = BasketPage(browser, link)
    basket_page.should_be_message_that_basket_empty()
    basket_page.basket_is_empty()
