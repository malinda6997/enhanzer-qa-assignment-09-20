import os
import json

import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage


load_dotenv()


@pytest.mark.order(2)
def test_employee_save(driver):

    # -------------------------
    # Load environment variables
    # -------------------------
    base_url = os.getenv("BASE_URL")
    username = os.getenv("EZUITE_USERNAME")
    password = os.getenv("EZUITE_PASSWORD")

    # -------------------------
    # Load JSON test data
    # -------------------------
    with open(
        "test_data/employee_data.json",
        "r",
        encoding="utf-8"
    ) as file:
        employee_data = json.load(file)

    data = employee_data[0]["general"]

    # Login
    login_page = LoginPage(driver)

    login_page.open(base_url)
    login_page.login(username, password)

    # Employee module
    employee_page = EmployeePage(driver)

    employee_page.click_employees()
    employee_page.click_new()


    employee_page.fill_employee_form(data)

    employee_page.upload_employee_image(
        os.path.abspath("test_data/employee.jpg")
    )

    employee_page.upload_attachment(
        os.path.abspath("test_data/test_attachment.pdf")
    )

    employee_page.click_save()