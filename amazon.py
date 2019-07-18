from selenium import webdriver
import account
import time

"Using the Firefox browser"
browser = webdriver.Chrome('/home/izzet/Downloads/chromedriver')

"Target site is Amazon.com"
browser.get("https://amazon.com")

"Go to log in page"
browser.find_element_by_id("nav-link-accountList").click()

"Email and password fields are selected and filled with the info from the 'account.py' file"
email = browser.find_element_by_id("ap_email")
password = browser.find_element_by_id("ap_password")
email.send_keys(account.mail)
password.send_keys(account.password)

"Logged in"
login = browser.find_element_by_id("signInSubmit")
login.click()

"Confirmed the the log in is successful"
accInfo = browser.find_element_by_class_name("nav-a.nav-a-2.nav-truncate")
accName = accInfo.text.find(account.name)

"Output of the account owner if the log in is successful"
if accName > -1 :
    print("Successfully entered to the account of "+ account.name)


"Select the search field and enter the desired product then select and click search button"
searchField = browser.find_element_by_id("twotabsearchtextbox")
searchButton = browser.find_element_by_class_name("nav-input")
searchField.send_keys("samsung")
searchButton.click()

"Confirm the result page is contains the desired product"
searchText = browser.find_element_by_class_name("a-color-state.a-text-bold")
if searchText.text.find('samsung') != -1:
    print("samsung is searched")

"Go to second second page"
pageButton = browser.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[7]/div/div/div/ul/li[3]/a")
pageButton.click()

"Click on the second product on the page"
product = browser.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
product.click()

"Get the products name"
productName = browser.find_element_by_xpath('//*[@id="productTitle"]').text


"Click on the 'Add list' button"
addList = browser.find_element_by_id('add-to-wishlist-button-submit')
addList.click()

time.sleep(2)


"Check if the product added to list is same "
listProductName = browser.find_element_by_xpath("//*[@id='WLHUC_info']/div[1]/ul/li[2]/table/tbody/tr/td/a").text


right = True
for i in range(25):
    if listProductName[i] != productName[i]:
        right = False

if right:
    print("Right product is added to wish list")

"Go to wish list page"
wishList = browser.find_element_by_xpath('//*[@id="WLHUC_viewlist"]/span/span')
wishList.click()

time.sleep(5)

deleteProduct = browser.find_element_by_css_selector('#a-autoid-7 > span > input')
deleteProduct.click()

deletedProductName = browser.find_element_by_css_selector('li.a-spacing-none:nth-child(2) > span:nth-child(1)').text
right = True
for i in range(25):
    if productName[i] != deletedProductName[i]:
        right = False

if right:
    print("Right product is deleted from wish list")

time.sleep(4)
browser.close()
browser.quit()
