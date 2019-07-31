from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.wishlist_page import WishlistPage
from base.page_base import PageBase

class AddListPopup(PageBase):
    """ """

    ADDED_PRODUCT = (By.ID, 'WLHUC_info')
    VIEW_WISH_LIST_BTN = (By.ID, 'WLHUC_viewlist')

    def __init__(self, driver):
        super(AddListPopup, self).__init__(driver)

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.VIEW_WISH_LIST_BTN), 'View wish list button '
                                                                                   'is not visible')
        self.wait.until(ec.visibility_of_element_located(self.ADDED_PRODUCT), 'Added product information '
                                                                              'is not visible')

    def click_view_wish_list_btn(self):
        """Click to view your list button and returns the Wish list page"""
        self.wait_for_element(self.VIEW_WISH_LIST_BTN).click()
        return WishlistPage(self.driver)

    def get_added_product(self):
        """Return the name of the product """
        return self.wait_for_element_visible(self.ADDED_PRODUCT).text.split('\n')[0]

