from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    def login_username(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        username_input.send_keys(username)

    def click_next_button(self):
        next_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Next']")
            )
        )
        next_button.click()

    def login_password(self, password):
        password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        self.wait.until(
            lambda driver: password_input.is_displayed()
        )

        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Login']")
            )
        )
        login_button.click()
        
    def click_yes_button(self):
        yes_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "loginwarningactionbutton")
            )
        )
        yes_button.click()

    def login(self, username, password):
        self.login_username(username)
        self.click_next_button()
        self.login_password(password)
        self.click_login_button()
        self.click_yes_button()