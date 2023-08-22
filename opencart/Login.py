from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")#launching the brower
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Lasen1@gmail.com")#email
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Lasen@123")

driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()#login
time.sleep(3)
current_url=driver.current_url
print(current_url)
if current_url!="https://demo.nopcommerce.com/login?returnurl=%2F":

    driver.find_element(By.XPATH,"//a[@class='ico-account']").click()#myaccount

    customer_information=driver.find_element(By.XPATH,"//ul[@class='list']//li[1]")#customerinformation
    customer_information.click()
    time.sleep(2)

    address=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[2]/a")#address
    address.click()
    time.sleep(2)


    orders=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[3]/a")#customerinformation
    orders.click()
    time.sleep(2)

    downloadable_product=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[4]/a")
    downloadable_product.click()
    time.sleep(2)

    back_in_stock_subscrib=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[5]/a")
    back_in_stock_subscrib.click()
    time.sleep(2)

    reward_point=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[6]/a")
    reward_point.click()
    time.sleep(2)

    change_password=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[7]/a")
    change_password.click()
    time.sleep(2)


    my_product_reviews=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[8]/a")
    my_product_reviews.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()  # logout
    time.sleep(5)
elif current_url=="https://demo.nopcommerce.com/login?returnurl=%2F":
    msg=driver.find_element(By.XPATH,"//div[@class='message-error validation-summary-errors']").text
    print(msg)









driver.close()
driver.quit()