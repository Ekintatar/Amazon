from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.wishlist_page import WishlistPage
from pages.add_list_popup import AddListPopup
from base.page_base import PageBase

class ProductPage(PageBase):
    """ """
    ADD_LIST_BTN = (By.ID, 'add-to-wishlist-button-submit')
    PRODUCT_NAME = (By.ID, 'productTitle')


    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.ADD_LIST_BTN), 'Add to list button is not visible!')
        self.wait.until(ec.visibility_of_element_located(self.PRODUCT_NAME), 'Product name is not visible!')

    def get_product_name(self):
        """Returns displayed product's name"""
        return self.get_element(self.PRODUCT_NAME).text.split('\n')[0]

    def click_add_list_btn(self):
        """Click 'Add list' button and return add list popup"""
        self.get_element(self.ADD_LIST_BTN).click()
        return AddListPopup(self.driver)
