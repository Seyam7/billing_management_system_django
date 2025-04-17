from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create your tests here.
class LoginFormTest(LiveServerTestCase):
    def formtest(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/auth/')

        time.sleep(3)
        user_name = driver.find_element_by_name('username')
        user_pass = driver.find_element_by_name('password')
        time.sleep(3)
        submit = driver.find_element_by_value('Login')

        user_name.send_keys('admin')
        user_password.send_keys('admin')
        submit.send_keys(Keys.RETURN)
