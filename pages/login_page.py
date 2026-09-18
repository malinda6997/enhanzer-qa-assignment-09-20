from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url)
        
     #Username page   
    def login_username(self, username):
        self.driver.find_element(By.ID, "userName").send_keys(username)
        
    def click_next_button(self):
        self.driver.find_element(By.XPATH, "//input[@value='Next']").click()
        
    #password page
    def login_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
    def login(self, username, password): 
        self.login_username(username)
        self.click_next_button()
        self.login_password(password)
        self.click_login_button()   
    


