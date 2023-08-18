from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datadriventesting import xcelutility
import time


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/search?q=books")#launching the brower
driver.maximize_window()
time.sleep(3)
file="c:\excel\search.xlsx"
row=xcelutility.getrowcount(file,"Sheet2")

for r in range(2,row+1):
    data=xcelutility.readdata(file,"Sheet2",r,1)
    driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys(data)
    driver.find_element(By.XPATH,"//button[@class='button-1 search-box-button']").click()
    time.sleep(2)

driver.close()
driver.quit()

