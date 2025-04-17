from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create your tests here.
class Hosttest(LiveServerTestCase):
    def testproductdetails(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/auth/')
        time.sleep(2)
        user_name = driver.find_element(By.NAME, "username")
        user_pass = driver.find_element(By.NAME, "password")
        time.sleep(3)
        submit = driver.find_element(By.NAME, "login")

        user_name.send_keys('admin')
        user_pass.send_keys('admin')
        submit.send_keys(Keys.RETURN)
