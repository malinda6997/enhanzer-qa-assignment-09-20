from selenium import webdriver


def test_open_browser():
    driver = webdriver.Chrome()

    driver.get("https://uat.ezuite.com/")

    print("Page title:", driver.title)

    driver.quit()