from django.test import TestCase,LiveServerTestCase
from selenium import webdriver
import time

# Create your tests here.
class BuyerTest(LiveServerTestCase):
    def listtest(self):
        driver2 = webdriver.Chrome()
        driver2.get('http://127.0.0.1:8000/buyerdetails/')
        time.sleep(5)
