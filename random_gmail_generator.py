import time
from selenium import webdriver
# Step 1: Download ChromeDriver from here: https://chromedriver.chromium.org/downloads/version-selection
# Step 2: Add the directory of the ChromeDriver to your PATH variable

##############################################################################################
class email:
    def __init__(self, email, password):
        self.email = email
        self.password = password
##############################################################################################

class random_gmail_generator:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_site(self):
        self.driver.get('http://www.gmail.com/')

email = random_gmail_generator()
email.go_to_site()