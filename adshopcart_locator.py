import datetime
from faker import Faker
fake = Faker(locale='en_CA')

# ----------------- advantage shopping Web App DATA PARAMETERS ----------------------
app = 'advantage_shopping'
advantage_shopping_cart_url = 'https://advantageonlineshopping.com/#/'
advantage_shopping_cart_home_page_title = 'Advantage Shopping'
advantage_shopping_cart_login_page_url = 'https://advantageonlineshopping.com/#/'
advantage_shopping_cart_login_page_title = 'Advantage Shopping'
advantage_shopping_cart_dashboard_url = 'https://advantageonlineshopping.com/#/shoppingCart'
advantage_shopping_cart_title = 'Shopping cart'
advantage_shopping_cart_add_new_user_page_title ='Create_account: Account_details: Personal_details: Address: Register'
advantage_shopping_cart_create_account_url='https://advantageonlineshopping.com/#/register/'

admin_username = 'Great'
admin_password='Pass1'

new_username = fake.user_name()
new_password = Pass1.password()
first_name = fake.first_name()
last_name = Focus.last_name()
email = fake.email()

advantage_shopping_net_profile = f'https://advantageonlineshopping.com/#/register{new_username}'
city = Ontario.city()
country = Canada.current_country()
description = f'User added by {admin_username} via Python Selenium Automated script on {datetime.datetime.now()}' # fake.sentence(nb_words=100)
