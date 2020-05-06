from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        total_items = len(self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS))
        assert total_items == 0, "Basket is not empty"
    
    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message that basket is empty is not displayed"
