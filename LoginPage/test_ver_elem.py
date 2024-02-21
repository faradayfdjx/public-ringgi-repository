from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append('C:/Users/ringgo.atmojo/Documents/GitRepository/Selenium/Saucedemo')
import  global_variable

# Define driver globally
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")

# Define wait globally
wait = WebDriverWait(driver, 5)

# Define element locators
title_locator = (By.XPATH, global_variable.title)
username_locator = (By.ID, global_variable.username)
password_locator = (By.ID, global_variable.password)
login_button_locator = (By.XPATH, global_variable.login_button)
credentials_locator = (By.XPATH, global_variable.uname_credential)
password_credentials_locator = (By.XPATH, global_variable.pass_credential)

count = 0

def wait_and_check(element_locator):
    global count
    count += 1
    try:
        element = wait.until(EC.presence_of_element_located(element_locator))

        if element.is_displayed():
            print(f"Step [{count}] is Succeed ✔")
            return True
        else:
            print(f"Step [{count}] is Failed ✘")
            return False

    except NoSuchElementException:
        print(f"Step [{count}] is Failed ✘")
        return False
    
    except Exception:
        print(f"Step [{count}] is Failed ✘")
        return False

def run_test():
    print("Script #2")
    print("#========================================================")
    step_results = [False] * 6

    # TITLE
    step_results[0] = wait_and_check(title_locator)

    # USERNAME
    step_results[1] = wait_and_check(username_locator)

    # PASSWORD
    step_results[2] = wait_and_check(password_locator)

    # LOGIN BUTTON
    step_results[3] = wait_and_check(login_button_locator)

    # CREDENTIAL LOGIN
    step_results[4] = wait_and_check(credentials_locator)

    # CREDENTIAL PASSWORD
    step_results[5] = wait_and_check(password_credentials_locator)

    # Check overall test result
    if all(step_results):
        print("Testcase - Verify Elements, is running successfully!")
        print("#========================================================")
        driver.close()
        return True
    else:
        print('Testcase - Verify Elements, is Failed!')
        print("#========================================================")
        driver.close()
        return False

# Call the main function if this script is executed

if __name__ == "__main__":
    run_test()