import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_login(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("EZUITE_USERNAME")
    password = os.getenv("EZUITE_PASSWORD")

    login_page = LoginPage(driver)

    login_page.open(base_url)
    login_page.login(username, password)