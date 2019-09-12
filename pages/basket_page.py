from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_new_guest_basket_page(self):
        self.should_be_empty_cart_message()
        self.should_be_empty()

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS_LIST), 'Cart is not empty'

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.CART_EMPTY_MESSAGE), (
            'No empty cart message'
        )
