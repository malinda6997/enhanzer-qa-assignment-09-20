from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    def login_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "userName"))
        ).send_keys(username)

    def click_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Next']")
            )
        ).click()

    def login_password(self, password):
        password_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "password"))
        )

        password_input.click()
        password_input.send_keys(password)

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Login']")
            )
        ).click()

    def click_yes_button(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.ID, "loginwarningactionbutton")
                )
            ).click()

        except TimeoutException:
            pass

    def login(self, username, password):
        self.login_username(username)
        self.click_next_button()
        self.login_password(password)
        self.click_login_button()
        self.click_yes_button()