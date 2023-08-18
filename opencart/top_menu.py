from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")#launching the brower
driver.maximize_window()
time.sleep(3)

#computer
computer=driver.find_elements(By.XPATH,"//ul[@class='top-menu notmobile']/li[1]")
