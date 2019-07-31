from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from base.page_base import PageBase

class ProductListPage(PageBase):
    """ """

    SEARCHED_WORD = (By.CLASS_NAME, 'a-color-state.a-text-bold')
    CLICKABLE_NEXT_PAGES = (By.CSS_SELECTOR, '.a-section.s-border-bottom .a-normal')
    PRODUCTS = (By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal')

    def __init__(self, driver):
        super(ProductListPage, self).__init__(driver)

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.SEARCHED_WORD), 'Searched word is not visible!')
        self.wait.until(ec.visibility_of_all_elements_located(self.CLICKABLE_NEXT_PAGES), 'Clickable next pages '
                                                                                          'are not visible!')
        self.wait.until(ec.visibility_of_all_elements_located(self.PRODUCTS), 'Products are not visible!')


    def click_to_product(self, order):
        """
        Click to desired product on product list
        :param order: Order of the product on product list

        """
        self.get_element_list(self.PRODUCTS)[order-1].click()
        return ProductPage(self.driver)

    def click_to_next_page(self):
        """Click to next clickable page and returns product list page"""
        self.get_element_list(self.CLICKABLE_NEXT_PAGES)[0].click()
        return ProductListPage(self.driver)

    def get_searched_word(self):
        """Reunrs the searched product name"""
        return self.wait_for_element_visible(self.SEARCHED_WORD).text