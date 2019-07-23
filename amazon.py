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
browser.find_element(By.ID, "nav-link-accountList").click()

"Email and password fields are selected and filled with the info from the 'account.py' file"
browser.find_element(By.ID, "ap_email").send_keys(account.mail)
browser.find_element(By.ID, "ap_password").send_keys(account.password)

"Logged in"
browser.find_element(By.ID, "signInSubmit").click()

"Confirmed the the log in is successful"
accName = browser.find_element(By.CLASS_NAME, "nav-a.nav-a-2.nav-truncate").text.find(account.name)

"Output of the account owner if the log in is successful"
assert (accName > 0), ("Unable to enter to the account of " + account.name)


"Select the search field and enter the desired product then select and click search button"
browser.find_element(By.ID, "twotabsearchtextbox").send_keys("samsung"+ Keys.ENTER)

"Confirm the result page is contains the desired product"
searchText = browser.find_element(By.CLASS_NAME, "a-color-state.a-text-bold")
assert searchText.text.find('samsung') > -1 , ("samsung could not be searched")

"Go to second second page"
browser.find_elements(By.CSS_SELECTOR, '.a-section.s-border-bottom .a-normal')[0].click()


"Click on the third product on the page"
browser.find_elements(By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal')[2].click()


"Get the products name"
productName = browser.find_element(By.ID, 'productTitle').text.split(' w/')[0]


"Click on the 'Add list' button"
browser.find_element(By.ID, 'add-to-wishlist-button-submit').click()


"keep the name of the prodcut to check right product is added to list"
listProductName = WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.ID, 'WLHUC_info')))[0].text.split(' w/')[0]

assert listProductName == productName, "Right product is added to wish list"

"Go to wish list page"
browser.find_element(By.ID, 'WLHUC_viewlist').click()

"Delete the newly added product"
browser.find_element(By.CSS_SELECTOR, '#a-autoid-7 > span > input').click()

"Keep the name of the deleted product to check right product is deleted"
deletedProductName = WebDriverWait(browser, 3).until(ec.presence_of_all_elements_located((
    By.CSS_SELECTOR, '.a-row.a-spacing-none')))[0].text.split(' w/')[0]


assert productName == deletedProductName, "Deletion process is failed"

time.sleep(4)
browser.close()
browser.quit()



