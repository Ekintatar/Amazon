from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import account
import time


"Using the Chrome browser"
browser = webdriver.Chrome('Drivers/chromedriver')

"Target site is Amazon.com"
browser.get("https://amazon.com")

"Confirm the page is on amazon.com"
assert browser.find_element(By.ID, "nav-logo").is_displayed(), "page is not on amazon.com"

"Go to log in page"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, "nav-link-accountList"))).click()

"Email and password fields are selected and filled with the info from the 'account.py' file"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, "ap_email"))).send_keys(account.mail)
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, "ap_password"))).send_keys(account.password)

"Logged in"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, "signInSubmit"))).click()

"Confirmed the the log in is successful"
accName = WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.CLASS_NAME, "nav-a.nav-a-2.nav-truncate"))).text.find(account.name)

"Output of the account owner if the log in is successful"
assert (accName > 0), ("Unable to enter to the account of " + account.name)


"Select the search field and enter the desired product then select and click search button"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, "twotabsearchtextbox"))).send_keys("samsung"+ Keys.ENTER)

"Confirm the result page is contains the desired product"
searchText = WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.CLASS_NAME, "a-color-state.a-text-bold")))
assert searchText.text.find('samsung') > -1 , ("samsung could not be searched")

"Go to second second page"
WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.CSS_SELECTOR, '.a-section.s-border-bottom .a-normal')))[0].click()


"Click on the third product on the page"
WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal')))[2].click()


"Get the products name"
productName = WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, 'productTitle'))).text.split('\n')[0]


"Click on the 'Add list' button"
browser.find_element(By.ID, 'add-to-wishlist-button-submit').click()


"keep the name of the product to check right product is added to list"
listProductName = WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.ID, 'WLHUC_info')))[0].text.split('\n')[0]

assert listProductName == productName, "Right product is not added to wish list"

"Go to wish list page"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.ID, 'WLHUC_viewlist'))).click()

"Delete the newly added product"
WebDriverWait(browser, 3).until(ec.presence_of_element_located((
    By.CSS_SELECTOR, '#a-autoid-7 > span > input'))).click()

"Keep the name of the deleted product to check right product is deleted"
deletedProductName = WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.CSS_SELECTOR, '.a-row.a-spacing-none')))[0].text.split('\n')[0]


assert productName == deletedProductName, "Deletion process is failed"

time.sleep(4)
browser.close()
browser.quit()



