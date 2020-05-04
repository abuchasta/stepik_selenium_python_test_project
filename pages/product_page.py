from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
    
    def should_be_message_with_product_name(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert messages[0].text == product_name.text, "Product name in the message does not match added product"
   
    def should_be_message_with_basket_price(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert messages[2].text == price.text, "Backet price does not match product price"