from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
print("Launched Browser and Application:")
driver.maximize_window()
time.sleep(5)


#enter textbox for name,gmail,phone and address
print("* entering data in text box ")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Marian Bell")#for name
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Marian_Bell@gmail.com")#for gmail
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("454566")#for phone no
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("No:11,First Floor, JPY Apartment,3rd street ,Erode")#for address
time.sleep(5)



#for Radio button
print("*Radio Button")
driver.find_element(By.XPATH,"//input[@id='female']").click()#selecting female radio buttton
time.sleep(5)


#for chk box
print("*Check box")
driver.find_element(By.XPATH,"//input[@id='monday']").click()#for monday
driver.find_element(By.XPATH,"//input[@id='tuesday']").click()#for tuesday
driver.find_element(By.XPATH,"//input[@id='friday']").click()#for friday
driver.find_element(By.XPATH,"//input[@id='saturday']").click()#for saturday
time.sleep(5)




#for DropDown Box
print("*Dropdown Box")
dpcountry=driver.find_element(By.XPATH,"//select[@id='country']")
dpcount=Select(dpcountry)
dpcount.select_by_visible_text("India")#selecting India in dropdownbox
time.sleep(5)

#Again Dropdown Box for selecting colour
dpcolour=driver.find_element(By.XPATH,"//*[@id='colors']")
dpcl=Select(dpcolour)
dpcl.select_by_visible_text("White")
time.sleep(5)




#Date-picker
print("*Date Picker:")
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()#selecting the date button
#since it is like table we cant use send_keys
exp_month="January"
exp_year="2009"
exp_date="12"
while True:
    act_month=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[1]").text
    act_year=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[2]").text
    if act_year==exp_year and act_month==exp_month :
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()


#now selecting all datesin the table
alldates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")#when we copy xpath,it full table,we need all table 31 values,so we add"/tr/td/a"
for a in alldates:
    if exp_date == a.text:#note we use a.text
        a.click()
        break
time.sleep(5)


#alert window
print("*Alert Window")
driver.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()
alertwindowforokbutton=driver.switch_to.alert
alertwindowforokbutton.accept()#for ok button for handle alert window
time.sleep(5)

#for handling ok and cancle button in alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
alertwindowforcanclebutton=driver.switch_to.alert
alertwindowforcanclebutton.dismiss()
time.sleep(5)

#for passing text value and capture the text in alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
alertwindowforpassingtext=driver.switch_to.alert
print(alertwindowforpassingtext.text)
alertwindowforpassingtext.send_keys("BELIVE")
time.sleep(5)
alertwindowforpassingtext.dismiss()
time.sleep(5)



#all mouse operation
print("Double Click:")
#note:
#we need to import ActionChains package:from selenium.webdriver import ActionChains
fied1=driver.find_element(By.XPATH,"//input[@id='field1']")#capturing xpath for the textbox
fied1.clear()#clear the text
fied1.send_keys("Double click mouse")#passing new value to textbox
act=ActionChains(driver)
doubleclickcopybutton=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")#xpath for click button
act.double_click(doubleclickcopybutton).click().perform()#do click and do perform
time.sleep(5)



#Drag and drop operation
print("Drag and drop:")
sourceeelement=driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")#xpath for source element
targetelement=driver.find_element(By.XPATH,"//div[@id='droppable']")#xpath for target element
act=ActionChains(driver)#each mouse operation create action class object
act.drag_and_drop(sourceeelement,targetelement).perform()
time.sleep(5)




#slidder
print("Slidder:")

min_position=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
min_location=min_position.location
print("Staring point for slidder:",min_location)#Staring point for slidder: {'x': 890, 'y': 1089}
actslidder=ActionChains(driver)
actslidder.drag_and_drop_by_offset(min_position,50,0).perform()
time.sleep(5)
actslidder.drag_and_drop_by_offset(min_position,50,0).perform()
time.sleep(5)




#openning new browser window without tab Practice
print("new brower Window opened without TAB:",driver.title)
opennewwindow=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
opennewwindow.clear()
opennewwindow.send_keys("selenium")#search for selenium
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
alllinks=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div")#counting possible browser links
print("no of link available with selenuim",len(alllinks))#no of links available



driver.find_element(By.XPATH,"//*[@id='wikipedia-search-result-link']/a").click()#we click selenium in biology link
tabwindowcounting=driver.window_handles
print("no of windows oppened now :",len(tabwindowcounting))
tb1=tabwindowcounting[0]#selenium
tb2=tabwindowcounting[1]#automation practice
driver.switch_to.window(tb2)
time.sleep(5)
print("Title of  window:",driver.title)
driver.close()#we closed seleniu  window

driver.switch_to.window(tb1)
time.sleep(5)
print("Title of WIndow :",driver.title)
time.sleep(5)

#openning new browser window  tab Practice
#note:from selenium.webdriver.common import keys
print("new brower Window opened without TAB:",driver.title)
opennewwindow=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
opennewwindow.clear()
opennewwindow.send_keys("java")#search for selenium
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
act=ActionChains(driver)
act.send_keys(keys.Keys.TAB).perform()#for tab
act.send_keys(keys.Keys.TAB).perform()
act.send_keys(keys.Keys.ENTER).perform()#for enter key
#now we close currentwindow
javawindow=driver.window_handles
print("No Of windows opened :",len(javawindow))
driver.switch_to.window(javawindow[1])
time.sleep(5)
driver.close()
driver.switch_to.window(javawindow[0])
time.sleep(5)





print("\n")
#new browser window Pracitce
print("*New Browser Window")
print("Title :",driver.title)
driver.find_element(By.XPATH,"//*[@id='HTML4']/div[1]/button").click()
print("Title :",driver.title)
windowsID=driver.window_handles
print("\n No of windows Opened",len(windowsID))
print("Paren Window ID IS :",windowsID[0])
print("Child Window ID IS :",windowsID[1])

print("Switching between windows")
w1=windowsID[0]
w2=windowsID[1]

driver.switch_to.window(w1)
print("Title :",driver.title)#auto pract window
time.sleep(2)
driver.switch_to.window(w2)
print("Title :",driver.title)#your store window
#mouse-hoveraction
yourstorecomponentmenu=driver.find_element(By.XPATH,"//a[normalize-space()='Components']")
yourstorecomponentmenu_monitor2=driver.find_element(By.XPATH,"//a[normalize-space()='Monitors (2)']")
act=ActionChains(driver)
act.move_to_element(yourstorecomponentmenu).move_to_element(yourstorecomponentmenu_monitor2).click().perform()
time.sleep(5)

driver.switch_to.window(w1)#again to auto pract window
print("Title :",driver.title)
time.sleep(5)

driver.switch_to.window(w2)#again to your store and we close this window
time.sleep(5)
driver.close()

driver.switch_to.window(w1)
print("Title :",driver.title)
time.sleep(5)



#frame
print("Frames:")

frame1=driver.find_element(By.ID,"frame-one796456169")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//a[@class='item_anchor']/parent::div[1]/child::input[@id='RESULT_TextField-0']").send_keys("menon")
#above web element is dynamic,it took long time to locate it
driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-1_0']").click()#for selecting gender
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-2']").send_keys("12/10/2020")
jobdropdown=driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-3']")
jobdp=Select(jobdropdown)
jobdp.select_by_visible_text("Manager")
driver.find_element(By.XPATH,"//*[@id='FSsubmit']").click()
driver.switch_to.default_content()


print("Resizing the Image")
#Resizing the picture
#time.sleep(3)
toresizeobjet=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
driver.execute_script("arguments[0].scrollIntoView();",toresizeobjet)
acct=ActionChains(driver)

acct.drag_and_drop_by_offset(toresizeobjet,50,50).perform()
time.sleep(5)



print("Table Handling:")
print("Expected Results :Book name is Master In JS ")
expected_Book_name="Master In Selenium"
book_names=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td[1]")


i=2
for bkname in book_names:

    if bkname.text==(expected_Book_name):
        print(bkname.text)
        xpath_text="//table[@name='BookTable']//tr["+str(i)+"]"
        print(driver.find_element(By.XPATH,xpath_text).text)

    i=i+1




print("Pagination Table")
print("We select Product 7")
expected_product="Product 7"

total_page=driver.find_elements(By.XPATH,"//ul[@class='pagination']//li")
for ttpp in total_page:
    pgct=1
    product_list=driver.find_elements(By.XPATH,"//div[@class='table-container']//tr//td[2]")
    for ppll in product_list:
        if ppll.text==expected_product:
            print(ppll.text)
            xpath_selected_product="//div[@class='table-container']//tr["+str(pgct)+"]//td[4]//input"
            cliked_product=driver.find_element(By.XPATH,xpath_selected_product)
            cliked_product.click()
            time.sleep(2)


        pgct = pgct + 1
    ttpp.click()
    time.sleep(2)

print("Scroll Bar:")
#it comes from browser not from application(so Actionchain wont work)
#need  javascript:"window.scrollBy(0,document.body.scrollHeight)"
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)
print("Test Completed")
driver.quit()




