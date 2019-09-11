from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BUTTON = (By.CSS_SELECTOR, 'span > a')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    CART_TOTAL_MESSAGE = (By.CLASS_NAME, 'alert-info')
    CART_TOTAL_MESSAGE_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')


class BasketPageLocators:
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    CART_ITEMS_LIST = (By.CLASS_NAME, 'basket-items')
