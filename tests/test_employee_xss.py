import json
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(
    BASE_DIR,
    "test_data",
    "employee_xss_data.json"
)

with open(DATA_FILE, "r", encoding="utf-8") as file:
    test_data = json.load(file)


def is_xss_alert_executed(driver):
    try:
        WebDriverWait(driver, 2).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return True, alert_text
    except (TimeoutException, NoAlertPresentException):
        return False, None


def is_error_popup_displayed(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.ID, "errormessage")
            )
        )
        return True
    except TimeoutException:
        return False


@pytest.mark.parametrize(
    "data",
    test_data,
    ids=[item["id"] for item in test_data]
)
def test_xss_edge_case(driver, data):
    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    login_page.open("https://uat.ezuite.com/")
    login_page.login(
        "info@enhanzer.com",
        "Welcome#5"
    )

    employee_page.click_employees()
    employee_page.click_new()

    employee_page.fill_employee_form(data["general"])

    # Inject XSS payload into the selected field.
    field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.ID, data["field"])
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        field
    )

    field.click()
    field.clear()
    field.send_keys(data["payload"])

    # Save the employee.
    employee_page.click_save()

    # Check whether JavaScript executed.
    alert_executed, alert_text = is_xss_alert_executed(driver)

    # Check application error handling.
    error_popup = is_error_popup_displayed(driver)

    if alert_executed:
        pytest.fail(
            f"{data['id']} - XSS executed in {data['field_name']}. "
            f"Alert text: {alert_text}"
        )

    print(
        f"{data['id']} | "
        f"Field: {data['field_name']} | "
        f"Payload: {data['payload_id']} | "
        f"Alert executed: {alert_executed} | "
        f"Error popup: {error_popup}"
    )
    
    # Take screenshot after save.
    screenshot_dir = os.path.join(
        BASE_DIR,
        "screenshots"
    )

    os.makedirs(
        screenshot_dir,
        exist_ok=True
    )

    screenshot_path = os.path.join(
        screenshot_dir,
        f"{data['id']}.png"
    )

    driver.save_screenshot(
        screenshot_path
    )

    print(
        f"Screenshot saved: {screenshot_path}"
    )