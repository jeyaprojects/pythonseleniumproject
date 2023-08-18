from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datadriventesting import xcelutility
import time


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")#launching the brower
driver.maximize_window()
time.sleep(3)


file="C:\excel\sr.xlsx"
row=xcelutility.getrowcount(file,"Sheet1")
print(row)


for r in range(2,row+1):
    #reading data from excel
    gender=xcelutility.readdata(file,"Sheet1",r,1)
    first_name=xcelutility.readdata(file,"Sheet1",r,2)
    last_name = xcelutility.readdata(file, "Sheet1", r, 3)
    ex_day= xcelutility.readdata(file, "Sheet1", r, 4)
    ex_month = xcelutility.readdata(file, "Sheet1", r, 5)
    ex_year= xcelutility.readdata(file, "Sheet1", r, 6)
    gmail= xcelutility.readdata(file, "Sheet1", r, 7)
    company_name = xcelutility.readdata(file, "Sheet1", r, 8)
    password= xcelutility.readdata(file, "Sheet1", r, 9)
    confirm_password = xcelutility.readdata(file, "Sheet1", r, 10)
    print(gender,first_name,last_name,ex_day,ex_month,ex_year,gmail,company_name,confirm_password,password)

    #passing data to application
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()  # registor click
    gender_male=driver.find_element(By.XPATH, "//input[@id='gender-male']")  # gender
    gender_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
    if gender=="male":
        gender_male.click()
    else:
        gender_female.click()
    driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(first_name)  # firstname
    driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(last_name)  # lastname
    #time.sleep(2)

    # dob
    dpfordays = Select(driver.find_element(By.XPATH, "//select[@name='DateOfBirthDay']"))  # day
    dpfordays.select_by_visible_text(str(ex_day))
    #time.sleep(2)

    month = driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']")  # month
    dpformonth = Select(month)
    dpformonth.select_by_visible_text(str(ex_month))

    year = driver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']")  # year
    doforyear = Select(year)
    doforyear.select_by_visible_text(str(ex_year))

    driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(gmail)  # email
    driver.find_element(By.XPATH, "//input[@id='Company']").send_keys(company_name)  # company name

    # password
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys(confirm_password)

    driver.find_element(By.XPATH, "//button[@id='register-button']").click()
    #time.sleep(2)

    current_url=driver.current_url
    time.sleep(5)
    print(current_url)
    if current_url=="https://demo.nopcommerce.com/registerresult/1?returnUrl=/":
        print("successfully registored")
        xcelutility.writedata(file,"Sheet1",r,11,"Success")
        xcelutility.fillgreencolor(file,"Sheet1",r,11)
    elif current_url=="https://demo.nopcommerce.com/register?returnurl=%2F":
        print("Not Registor")
        xcelutility.writedata(file,"Sheet1",r,11,"Not Registor")
        xcelutility.fillredcolor(file,"Sheet1",r,11)
    else:
        print("Incomplete")
        xcelutility.writedata(file, "Sheet1", r, 11, " Registor incomplete")
        xcelutility.fillredcolor(file, "Sheet1", r, 11)


#https://demo.nopcommerce.com/register?returnurl=%2F


driver.close()
driver.quit()






