import os
import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage

load_dotenv()


@pytest.mark.order(2)
def test_employee_form(driver):

    base_url = os.getenv("BASE_URL")
    username = os.getenv("EZUITE_USERNAME")
    password = os.getenv("EZUITE_PASSWORD")

    # Login
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(username, password)

    # Employee page
    employee_page = EmployeePage(driver)
    employee_page.click_employees()
    employee_page.click_new()