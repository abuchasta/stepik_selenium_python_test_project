from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  
    page.open()
    page.press_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_with_product_name()
    page.should_be_message_with_basket_price()