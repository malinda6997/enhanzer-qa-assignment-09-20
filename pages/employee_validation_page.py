from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EmployeeValidationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_validation_popup_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.ID, "errormessage")
                )
            )
            return True
        except TimeoutException:
            return False

    def get_validation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "errormessage")
            )
        ).text.strip()

    def close_validation_popup(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@id='errorModal']//button[@data-dismiss='modal']"
                )
            )
        ).click()

    def click_save(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "saveNewEmployeeBtn")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            save_button
        )

        save_button.click()