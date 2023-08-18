from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")#launching the brower
driver.maximize_window()
time.sleep(3)
print("Website Opened for Testing")
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Mala Ravi")#entering name
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys("23423423")#entering phone no
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("sample@gmail.com")#entering mail id
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("mypassword123")#entering password
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("10.RV street,cochin")#entering address
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()#submit button
time.sleep(5)

driver.close()
driver.quit()
print("comlpled with text data")
#first switching to frame
