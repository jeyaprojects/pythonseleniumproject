from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")#launching the brower
driver.maximize_window()
time.sleep(3)
print("Website Opened for Testing")
#selecting radio button
driver.find_element(By.XPATH,"//input[@id='female']").click()#radio button for selecting female
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='male']").click()#radio button for selecting male
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='other']").click()#radio button for selecting other,but it not working
time.sleep(5)


#selecting chk boxes
driver.find_element(By.XPATH,"//input[@id='monday']").click()#chk box practice for monday to select
driver.find_element(By.XPATH,"//input[@id='sunday']").click()#chk box practice for sunday to select
driver.find_element(By.XPATH,"//input[@id='sunday']").click()#chk box practice for sunday to unselect


#finding total no of days in this chkbox
chklink=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print("Total chk boxes",len(chklink))

#to unselect the already selected chkboxes
for x in chklink:
    if x.is_selected():
        x.click()

#selecting all chk boxes at one single shot
for x in chklink:
    x.click()
time.sleep(5)

#dropdownbox
dpdown=driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div/select")#note it is find_element not elements
time.sleep(5)
dp=Select(dpdown)
dp.select_by_visible_text("Sweden")
time.sleep(5)



#Again chk boxes and radio button practice
driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[1]/div[2]/label").click()#radio button for2 years
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()#chkbox for selenium webdriver
driver.find_element(By.XPATH,"//label[normalize-space()='Testim']").click()#chkbox for testim
time.sleep(5)


driver.close()
driver.quit()
print("completed testing")