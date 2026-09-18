from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_loader(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.ID, "loaderwrapper")
            )
        )

    def fill_field_by_id(self, element_id, value):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, element_id)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        element.click()
        element.clear()
        element.send_keys(value)

    def select_by_id(self, element_id, value):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, element_id)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        Select(element).select_by_visible_text(value)

    def click_employees(self):
        self.wait_for_loader()

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[@href='/Distribute/DistributeMain/Employee']"
                )
            )
        ).click()

        self.wait_for_loader()

    def click_new(self):
        self.wait_for_loader()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "addNewEmployee")
            )
        ).click()

        self.wait_for_loader()

    def fill_employee_form(self, data):

        # Title
        self.select_by_id(
            "employeeSalutations",
            data["title"]
        )

        # Employee Name
        self.fill_field_by_id(
            "employeeName",
            data["name"]
        )

        # Initials
        self.fill_field_by_id(
            "empNameInitials",
            data["initials"]
        )

        # First Name
        self.fill_field_by_id(
            "empFirstName",
            data["first_name"]
        )

        # Last Name
        self.fill_field_by_id(
            "empLastName",
            data["last_name"]
        )

        # Address
        self.fill_field_by_id(
            "employeeAddress",
            data["address"]
        )

        # NIC
        self.fill_field_by_id(
            "employeeNic",
            data["nic"]
        )

        # Email
        self.fill_field_by_id(
            "employeeEmail",
            data["email"]
        )

        # Mobile
        self.fill_field_by_id(
            "employeeMobile",
            data["mobile"]
        )

        # Phone
        self.fill_field_by_id(
            "employeePhone",
            data["phone"]
        )

        # Reference
        self.fill_field_by_id(
            "employeeReference",
            data["reference"]
        )

        # Vehicle Number
        self.fill_field_by_id(
            "employeevehicleNo",
            data["vehicle_no"]
        )

        # Employee Status
        self.select_by_id(
            "EmployeeStatus",
            data["employee_status"]
        )

        # Designation
        self.fill_field_by_id(
            "employeeDesignation",
            data["designation"]
        )

        # EPF Number
        self.fill_field_by_id(
            "employeeEPFNo",
            data["epf_no"]
        )

        # Date Of Joined
        self.fill_field_by_id(
            "employeeDateJoined",
            data["date_of_joined"]
        )

        # Location
        self.fill_field_by_id(
            "employeeLocation",
            data["location"]
        )

        # Remark
        self.fill_field_by_id(
            "employeeRemark",
            data["remark"]
        )

        # Date Of Birth
        self.fill_field_by_id(
            "employeeDOB",
            data["date_of_birth"]
        )

        # Bank Name
        self.fill_field_by_id(
            "empBankName",
            data["bank_name"]
        )

        # Bank Account
        self.fill_field_by_id(
            "empBankAccount",
            data["bank_account"]
        )

        # Bank Code
        self.fill_field_by_id(
            "empBankCodeNum",
            data["bank_code"]
        )

        # Employee Group
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "EZCMP1/EZLOC16/EZEMPG-2_anchor"
                )
            )
        ).click()

    def upload_employee_image(self, file_path):

        image_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "file")
            )
        )

        image_input.send_keys(file_path)

    def upload_attachment(self, file_path):

        attachment_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "files")
            )
        )

        attachment_input.send_keys(file_path)

    def click_save(self):

        self.wait_for_loader()

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

        self.wait_for_loader()