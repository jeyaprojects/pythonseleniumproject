from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")#launching the brower
driver.maximize_window()
time.sleep(3)

search_item=driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("Shoes")
time.sleep(2)


search_button=driver.find_element(By.XPATH,"//button[normalize-space()='Search']")
search_button.click()
time.sleep(5)

sort_by_shoes=driver.find_element(By.XPATH,"//select[@id='products-orderby']")
dp_sort_by_shoes=Select(sort_by_shoes)
dp_sort_by_shoes.select_by_visible_text("Position")
time.sleep(2)
dp_sort_by_shoes.select_by_visible_text("Name: A to Z")
time.sleep(2)
dp_sort_by_shoes.select_by_visible_text("Name: Z to A")
time.sleep(2)
dp_sort_by_shoes.select_by_visible_text("Price: Low to High")
time.sleep(2)
dp_sort_by_shoes.select_by_visible_text("Price: High to Low")
time.sleep(2)
dp_sort_by_shoes.select_by_visible_text("Created on")
time.sleep(2)

display_by_nos_shoes=driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
dp_display_by_nos_shoes=Select(display_by_nos_shoes)
dp_display_by_nos_shoes.select_by_visible_text("3")
time.sleep(2)
dp_display_by_nos_shoes.select_by_visible_text("6")
time.sleep(2)
dp_display_by_nos_shoes.select_by_visible_text("9")
time.sleep(2)
dp_display_by_nos_shoes.select_by_visible_text("18")
time.sleep(2)

driver.close()
driver.quit()
