from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.page_base import PageBase

class LoginPage(PageBase):
    """ """

    EMAIL_INPUT = (By.ID, 'ap_email')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    LOGIN_BTN = (By.ID, "signInSubmit")
    LOGIN_MESSAGE = (By.ID, 'auth-warning-message-box')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.EMAIL_INPUT), 'Email input field is not visible')
        self.wait.until(ec.visibility_of_element_located(self.PASSWORD_INPUT), 'Password input field is not visible')
        self.wait.until(ec.visibility_of_element_located(self.LOGIN_BTN), 'Login button is not visible')

    def clear_email_input(self):
        """Clear 'email' input"""
        self.get_element(self.EMAIL_INPUT).clear()

    def clear_password_input(self):
        """Clear 'password' input"""
        self.get_element(self.PASSWORD_INPUT).clear()

    def click_to_login_btn(self):

        """Click to login button and returns the main page"""
        self.get_element(self.LOGIN_BTN).click()


    def fill_login_form(self, email, password):
        """Fills login&pass inputs in login form"""
        self.get_element(self.EMAIL_INPUT).send_keys(email)
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def is_login_message_visible(self):
        """Returns warning message if it exists"""
        return self.wait_for_element_visible(self.LOGIN_MESSAGE)