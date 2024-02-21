from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import sys, os

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")

def run_test():
    send_title = "Swag Labs"
    title = driver.title
    try:
        print("#========================================================")
        print("Script #1")
        print("#========================================================")
        assert title == send_title, f"Expected is '{driver.title}' while the Actual is '{send_title}'"

    except AssertionError as e:
        print(f"Step [1] : Failed to Validate Webpage Title!")
        print("Failed when running the step!")
        print("#========================================================")
        driver.close()
        return False

    else:
        print("Step [1] : Success to Validate Webpage Title!")
        print("Testcase Succeed! Stopping the program.")
        print("#========================================================")
        driver.close()
        return True

if __name__ == "__main__":
    run_test()
