from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_click(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_message_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), (
            'No \"added to cart\" message'
        )

    def should_be_same_product_name(self):
        product_name_header = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_CART_PRODUCT
        ).text
        assert product_name_header == product_name_message, (
            'Product name is not same in \"added to cart\" message'
        )

    def should_be_same_cart_and_product_price(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element(
            *ProductPageLocators.CART_TOTAL_MESSAGE_PRICE
        ).text
        assert product_price_on_page == product_price_in_message, (
            'Product price is not same in \"cart total\" message'
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), (
            'Add to cart successful message is present, but should not be'
        )

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_CART_MESSAGE), (
            'Add to cart successful message has not disappeared'
        )
