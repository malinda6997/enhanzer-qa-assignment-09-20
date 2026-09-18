from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_loader(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.ID, "loaderwrapper")
            )
        )

    def click_employees(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/Distribute/DistributeMain/Employee']")
            )
        ).click()

    def click_new(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@id='addNewEmployee']")
            )
        ).click()

    def click_save(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@id='saveNewEmployeeBtn']")
            )
        ).click()