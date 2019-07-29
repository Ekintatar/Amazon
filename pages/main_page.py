from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from base.page_base import PageBase


class MainPage(PageBase):
    """Main page https://www.amazon.com/"""

    ACCOUNT = (By.ID, 'nav-link-accountList')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    ACCOUNT_INFO = (By.ID, 'nav-a.nav-a-2.nav-truncate')

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.SEARCH_INPUT), 'Search field is not visible')

    def search_product(self, product_name):
        """Fills and searches desired product and returns the product list page"""
        self.get_element(self.SEARCH_INPUT).send_keys(product_name + Keys.ENTER)
        return ProductListPage(self.driver)

    def click_account(self):
        """Click to the account element and returns the login panel"""
        self.wait_for_element(self.ACCOUNT).click()
        return LoginPage(self.driver)

    def get_acc_info(self):
        """Returns user account information"""
        return self.get_element(self.ACCOUNT_INFO).text