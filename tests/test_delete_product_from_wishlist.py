import logging
from unittest import TestCase
from selenium import webdriver
from pages.main_page import MainPage
from base.base_test import *
import os


@decorator_loader(error_logger)
class TestDeleteProductFromWishlist(TestCase):

    """Test case is:

        1. Enter 'www.amazon.com' and check that it is main page
        2. Open login panel and login as a user
        3. In the search area on the top of the screen write 'samsung' and search it
        4. From the incoming page check the results related to samsung
        5. From result page click second page option ad check the page is on second page
        6. Click 'Add to List' option on third product
        7. Click 'List' link from the top of the screen and choose Wish List option
        8. Check the product we added to the list is present in the list
        9. Click 'Delete' button of the newly added product and remove from the wish list
        10. Check the product is no longer in wish list.

        """

    fileDir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(fileDir)


    CHROME_DRIVER_PATH = path + '/Drivers/chromedriver'

    def setUp(self):
        self.driver = webdriver.Chrome(self.CHROME_DRIVER_PATH)
        width = self.driver.execute_script("return window.screen.availWidth")
        height = self.driver.execute_script("return window.screen.availHeight")
        self.driver.set_window_size(width, height)
        self.driver.get('https://amazon.com')
        print("TestDeleteProductFromWishlist")


    def test_delete_product_from_wishlist(self):
        """Test checks deletion of the newly added Samsung product from the wish list"""

        main_page = MainPage(self.driver)
        login_page = main_page.click_account()
        print("Successfully entered to the main page")

        login_page.fill_login_form('tatarekinez@hotmail.com', 'ekinwelcome')
        login_page.click_to_login_btn()

        print('Successfully logged in to the account of ' + 'ekin')

        product_list_page = main_page.search_product('samsung')
        second_product_list_page = product_list_page.click_to_next_page()
        product_page = second_product_list_page.click_to_product(3)
        product_name = product_page.get_product_name()
        popup = product_page.click_add_list_btn()
        added_product_name = popup.get_added_product()
        assert(added_product_name == product_name, 'Added product name is different')
        print("Product is added to the wish list!")


        wish_list_page = popup.click_view_wish_list_btn()
        wish_list_page.click_delete_btn()
        deleted_product_name = wish_list_page.get_deleted_product_name()
        assert(deleted_product_name == added_product_name, 'Deleted product name is different')
        print("Product is deleted from wish list!")


    def tearDown(self):
        self.driver.quit()
