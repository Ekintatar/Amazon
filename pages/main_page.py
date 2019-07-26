from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.page_base import PageBase

class MainPage(PageBase):
    """Main page https://www.amazon.com/"""

    ACCOUNT = (By.ID, 'nav-link-accountList')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.ACCOUNT), 'Account button is not visible')
        self.wait.until(ec.visibility_of_element_located(self.SEARCH_INPUT), 'Search field is not visible')

    def send_keys_to_search_input(self, product_name):
        """Fills search input"""
        self.get_element(self.SEARCH_INPUT).send_keys(product_name)

    def search_product(self):
        """Search desired product"""
        self.get_element(self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def click_account(self):
        """Click to the account element"""
        self.get_element(self.ACCOUNT).click()