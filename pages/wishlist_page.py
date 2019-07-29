from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.page_base import PageBase

class WishlistPage(PageBase):
    """ """

    DELETE_BTN = (By.CSS_SELECTOR, '#a-autoid-7 > span > input')
    DELETED_PRODUCT_NAME = (By.CLASS_NAME, 'a-row.a-spacing-none')

    def __init__(self, driver):
        super(WishlistPage, self).__init__(driver)

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.DELETE_BTN), 'Delete button for the the desired '
                                                                           'product is not visible')

    def click_delete_btn(self):
        """Click to delete button"""
        self.get_element(self.DELETE_BTN).click()

    def get_deleted_product_name(self):
        """Returns deleted product name"""
        return self.get_element_list(self.DELETED_PRODUCT_NAME)[0].text.split(' \n')[0]