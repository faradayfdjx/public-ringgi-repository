from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import sys
sys.path.append('C:/Users/ringgo.atmojo/Documents/GitRepository/Selenium/Saucedemo')
import global_variable

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver, 5)

username_locator = (By.ID, global_variable.username)
password_locator = (By.ID, global_variable.password)
login_button_locator = (By.XPATH, global_variable.login_button)

user_val = global_variable.username_one
pass_val = global_variable.password_val

fail_cont = (By.XPATH, global_variable.fail_container)
fail_cta = "Epic sadface: Sorry, this user has been locked out."
count_check = 0

def input_check(element_input, val):
    global count_check
    count_check += 1
    try:
        attr = wait.until(EC.presence_of_element_located(element_input))

        if attr.is_displayed():
            attr.send_keys(val)
            attr.send_keys(Keys.RETURN)
            print(f"Step [{count_check}] input '{val}' as {element_input} is Succeed ✔")
            return True
        
        else:
            print(f"Step [{count_check}] input '{val}' as {element_input} is Failed ✘")
            return False
           
    except Exception as e:
        print(f"Can't handle the process!")
        return False

def direct_login():
    exp_url = "https://www.saucedemo.com/"
    try:
        element = wait.until(EC.presence_of_element_located(login_button_locator))
        
        if element.is_displayed():
            element.click()
            url = driver.current_url
            
            try:
                fail_obj = wait.until(EC.presence_of_element_located(fail_cont))
                fail_txt = driver.find_element(By.XPATH, global_variable.cta_fail).get_attribute("textContent")
                print(fail_cta)
                print(url)
                assert url == exp_url, f"URL is not the same, expected {exp_url}"
                assert fail_cta == fail_txt, f"Expected is '{fail_txt}' while the Actual is '{fail_cta}'"

            except TimeoutException:
                print("Timeout Error!")
                return False

            except NoSuchElementException as e:
                print("No such element found!")
                return False
                    
            except AssertionError:
                print("Unmatched CTA / URL text, check on either one of those!")
                return False
                    
            else:
                if fail_obj.is_displayed() : #and url == exp_url and fail_cta == fail_txt:
                    print(f"Step [2] click and show fail is Succeed ✔")
                    return True
                
                else:
                    print(f"Step [2] click and show fail is Failed ✘")
                    print(url)
                    return False
        else:
            print("Can't handle the process!")
            return False
        
    except NoSuchElementException:
        print("Element not Found!")
        return False


def run_test():
    print("Test Started...")
    step_results = [False] * 3
    
    # USERNAME
    print("=======================================================")
    step_results[0] = input_check(username_locator, user_val)

    # PASSWORD
    step_results[1] = input_check(password_locator, pass_val)

    # CLICK LOGIN
    step_results[2] = direct_login()

    # Check overall test result
    if all(step_results):
        print("Testcase - Failed Login, is running successfully!")
        print("=======================================================")
        driver.close()
        return True
    else:
        print('Testcase - Failed, is Failed!')
        print("=======================================================")
        driver.close()
        return False

# Call the main function if this script is executed

if __name__ == "__main__":
    run_test()