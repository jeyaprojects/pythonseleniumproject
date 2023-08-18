import unittest
import time
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("..//python2023")
from pageObject.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="http://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
    def test_Login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        lp.clickLout()
        time.sleep(2)
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\python2023\\reports'))

"""
to run in terminal to get htnal report
python -m testCases.LoginTest
"""