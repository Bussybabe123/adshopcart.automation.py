import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Advantage Shopping Test Automation Plan
# launch Advantage Shopping App website - validate we are on the home page
# navigate to Login page - validate we are on the login page
#create new account and register
#Input:
#Username generated
#Password generated
#User’s profile created
#user’s address added
#Phone number generated
#Acknowledge the user’s terms and condition
#click on the sign in button.
#Advantage shopping cart pops up- our products, special offer, popular item, contact us, users , cart
#Click on the product (product description stated)
#No order made
#sign out of the account.

'Actual_result'
print ('user sign in successfully')


'Result'

print ('User had access to the shopping cart account,but no order made')


# populate the new user form fields using Faker library fake random data# navigate to Add New User page - sign in new username or password - validate we are on the Add new User page
# use a new username and password to sign in
# incorrect username or password pops up.
#Sign in using new username and password.
#username account and select My Account.
#'Delete Account'
# log in again with non-existing username or password.
# incorrect username or password pops up.




def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------~*~--------------------------')
    # make browswer full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to advantage shopping website
    driver.get(locators.advantage_shopping_url)
    # check that advantage shopping URL and the home page title are as expected
    if driver.current_url == locators.advantage_shopping_Url and driver.title == locators.advantage_shopping_home_page_title: # check we are on the login page
        print(f'hurray! {locators.app} log in and sign out successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.30)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.30)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.advantage_shopping_url:  # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.advantage_shopping_login_page_url and driver.title == locators.advantage_shopping_login_page_title: # check we are on the login pag
            print(f'{locators.app} App Login page is displayed! Continue to log in.')
            sleep(0.30)
            driver.find_element(By.ID, 'username').send_keys(locators.admin_username)
            sleep(0.30)
            driver.find_element(By.ID, 'password').send_keys(locators.admin_password)
            sleep(0.30)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate login successful - Dashboard page is displayed
            if driver.current_url == locators.advantage_shopping_dashboard_url and driver.title == locators.advantage_shopping_dashboard_title:
                assert driver.current_url == locators.advantage_shopping_dashboard_url
                assert driver.title == locators.advantage_shopping_dashboard_title
                print(f' ---- Login is successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code or website and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.30)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.30
    if driver.current_url == locators.advantage_shoppinge_url
        print(f' ---- Logout successful! {datetime.datetime.now()}')


def create_new_user():
    # Navigate to 'Add a new user' form
    driver.find_element(By.XPATH, '//span[contains(.,'advantage_shopping']').click()
    sleep(0.30)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    linkchek = driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    print(f' ---- User link is displayed: {linkchek}')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.30)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.30)
    # Validate we are on 'Add a new user' page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.advantage_shopping_add_new_user_page_title
    print(f' ---- Navigate to Add a new user page - Page Title: {driver.title}')
    sleep(0.30)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.30)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.30)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.30)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.30)
    driver.find_element(By.ID,'id_lastname').send_keys(locators.last_name)
    sleep(0.30)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.30)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.30)
    driver.find_element(By.ID, 'id_advantage_shoppingnetprofile').send_keys(locators.advantage_shopping_net_profile
    sleep(0.30)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.30)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.30)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_value('America/Ontario')
    sleep(0.30)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.30)

    # upload picture
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    img_path = ['our products', 'special offer', 'shopping cart', 'popular items', 'contact us']
    for path in img_path:
        driver.find_element(By.LINK_TEXT, path).click()
        sleep(0.30)

    breakpoint()




# Launch app
setUp()
# Login
log_in()
# Create New User
create_new_user()
# Logout
log_out()
# Close app
tearDown()