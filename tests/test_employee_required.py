import json
import os

import pytest

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from pages.employee_validation_page import EmployeeValidationPage


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "test_data",
    "employee_required_data.json"
)


with open(DATA_FILE, "r", encoding="utf-8") as file:
    test_data = json.load(file)


@pytest.mark.parametrize(
    "data",
    test_data,
    ids=[item["id"] for item in test_data]
)
def test_missing_required_fields(driver, data):

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    validation_page = EmployeeValidationPage(driver)

    # Login

    login_page.open("https://uat.ezuite.com/")

    login_page.login(
        "info@enhanzer.com",
        "Welcome#5"
    )

    # Open Employee Form

    employee_page.click_employees()
    employee_page.click_new()

    # Enter Test Data

    employee_page.fill_employee_form(
        data["general"]
    )

    # Save

    validation_page.click_save()

    # Check Validation

    popup_displayed = (
        validation_page.is_validation_popup_displayed()
    )

    if popup_displayed:

        message = validation_page.get_validation_message()

        print(
            f"{data['id']} - Validation message: {message}"
        )

        validation_page.close_validation_popup()

    else:

        pytest.fail(
            f"{data['id']} - Required field was empty, "
            f"but validation popup was not displayed."
        )