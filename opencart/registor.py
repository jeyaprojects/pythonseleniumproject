from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")#launching the brower
driver.maximize_window()
time.sleep(3)


driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()#registor click

#personel details
driver.find_element(By.XPATH,"//input[@id='gender-male']").click()#gender
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Lasen")#firstname
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Aran")#lastname

day=driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']")#dob
dpfordays=Select(day)#day
dpfordays.select_by_visible_text("12")

month=driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']")#month
dpformonth=Select(month)
dpformonth.select_by_visible_text("December")

year=driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']")#year
doforyear=Select(year)
doforyear.select_by_visible_text("2000")

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Lasen1@gmail.com")#email
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("XYZABC")#company name

#password
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Lasen@123")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("Lasen@123")

driver.find_element(By.XPATH,"//button[@id='register-button']").click()

title=driver.current_url
print(title)
if title=="https://demo.nopcommerce.com/registerresult/1?returnUrl=/":
    chkregyes = driver.find_element(By.XPATH, "//div[@class='result']").text
    print(chkregyes)
    if chkregyes == "Your registration completed":
        driver.close()
    time.sleep(3)
    # driver.close()
else:
    # tochk registoration
    chkregno = driver.find_element(By.XPATH, "//form[@method='post']//li").text
    print(chkregno)
    if chkregno == "The specified email already exists":
        pass



driver.quit()

#your personal details
