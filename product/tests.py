from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Create your tests here.
class Hosttest(LiveServerTestCase):
    def testproductdetails(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/auth')
        time.sleep(2)
        user_name = driver.find_element(By.ID, "username")
        user_pass = driver.find_element("name", "password")
        time.sleep(3)
        submit = driver.find_element("name", "Login")

        user_name.send_keys('admin')
        user_password.send_keys('admin')
