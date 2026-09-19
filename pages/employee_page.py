from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Common Methods

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

    # Employee Navigation

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

    # Tab 1 - Employee Information

    def fill_employee_form(self, data):

        self.select_by_id(
            "employeeSalutations",
            data["title"]
        )

        self.fill_field_by_id(
            "employeeName",
            data["name"]
        )

        self.fill_field_by_id(
            "empNameInitials",
            data["initials"]
        )

        self.fill_field_by_id(
            "empFirstName",
            data["first_name"]
        )

        self.fill_field_by_id(
            "empLastName",
            data["last_name"]
        )

        self.fill_field_by_id(
            "employeeAddress",
            data["address"]
        )

        self.fill_field_by_id(
            "employeeNic",
            data["nic"]
        )

        self.fill_field_by_id(
            "employeeEmail",
            data["email"]
        )

        self.fill_field_by_id(
            "employeeMobile",
            data["mobile"]
        )

        self.fill_field_by_id(
            "employeePhone",
            data["phone"]
        )

        self.fill_field_by_id(
            "employeeReference",
            data["reference"]
        )

        self.fill_field_by_id(
            "employeevehicleNo",
            data["vehicle_no"]
        )

        self.select_by_id(
            "EmployeeStatus",
            data["employee_status"]
        )

        self.fill_field_by_id(
            "employeeDesignation",
            data["designation"]
        )

        self.fill_field_by_id(
            "employeeEPFNo",
            data["epf_no"]
        )

        self.fill_field_by_id(
            "employeeDateJoined",
            data["date_of_joined"]
        )

        self.fill_field_by_id(
            "employeeLocation",
            data["location"]
        )

        self.fill_field_by_id(
            "employeeRemark",
            data["remark"]
        )

        self.fill_field_by_id(
            "employeeDOB",
            data["date_of_birth"]
        )

        self.fill_field_by_id(
            "empBankName",
            data["bank_name"]
        )

        self.fill_field_by_id(
            "empBankAccount",
            data["bank_account"]
        )

        self.fill_field_by_id(
            "empBankCodeNum",
            data["bank_code"]
        )

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

    # Employee Edit

    def edit_employee(self, employee_name):

        row = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//tr[@ng-repeat='row in displayedCollection']"
                    f"[.//td[normalize-space()='{employee_name}']]"
                )
            )
        )

        edit_button = row.find_element(
            By.CSS_SELECTOR,
            "button.smart-button-edit"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_button
        )

        self.wait.until(
            lambda driver:
            edit_button.is_displayed()
            and edit_button.is_enabled()
        )

        for _ in range(3):

            try:
                edit_button.click()
                break

            except ElementClickInterceptedException:

                self.driver.execute_script(
                    """
                    document.querySelectorAll(
                        'div.modal-backdrop'
                    ).forEach(function(element) {
                        element.remove();
                    });
                    """
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    edit_button
                )

        self.wait_for_loader()

    # Tab 2 - Social Media

    def click_social_media_tab(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "Customized_SocialMediaTab")
            )
        ).click()

    def fill_social_media(self, data):

        self.fill_field_by_id(
            "employeeLinkedIn",
            data["linkedin"]
        )

        self.fill_field_by_id(
            "employeeFaceBook",
            data["facebook"]
        )

        self.fill_field_by_id(
            "employeeInstagram",
            data["instagram"]
        )

    # Tab 3 - Contacts

    def click_contacts_tab(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "customized_customContactDetailsTab")
            )
        ).click()

    def fill_contact(self, data):

        self.fill_field_by_id(
            "nameEmployeeContact",
            data["name"]
        )

        self.fill_field_by_id(
            "designationEmployeeContact",
            data["designation"]
        )

        self.select_by_id(
            "typeEmployeeContact",
            data["type"]
        )

        self.fill_field_by_id(
            "descriptionEmployeeContact",
            data["description"]
        )

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "contactAddData")
            )
        ).click()

    # Final Update

    def click_update(self):

        update_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "editEmployeeBtn")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            update_button
        )

        update_button.click()

        self.wait_for_loader()