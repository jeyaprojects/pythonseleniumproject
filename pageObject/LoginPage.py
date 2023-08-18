from selenium.webdriver.common.by import By


class LoginPage():
    #locators for all elements
    textbox_email_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    button_logout_xpath="//a[normalize-space()='Logout']"


    #create contructor and initate the driver
    def __init__(self,driver):
        self.driver=driver
    #create action method for each element
    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def clickLout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()



