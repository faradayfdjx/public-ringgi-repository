from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append('C:/Users/Admin/Documents/selenium/Python')
import global_variable

# IMPORTANT VARIABLE DECLARATION ======================================
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 5)

username_locator = (By.ID, global_variable.username)
login_button_locator = (By.XPATH, global_variable.login_button)

user_val = global_variable.username_one 
#pass_val = global_variable.password_val

fail_cont = (By.XPATH, global_variable.fail_container)
cta_text = "Epic sadface: Password is required"

count_check = 0
# IMPORTANT VARIABLE DECLARATION ======================================


def input_check(element_input, val):
    global count_check
    count_check += 1
    try:
        attr = wait.until(EC.presence_of_element_located(element_input))

        if attr.is_displayed():
            attr.send_keys(val)
            attr.send_keys(Keys.RETURN)
            print(f"Step [{count_check}] input '{val}' as {element_input} is Succeed ✔")

            exp_url = "https://www.saucedemo.com/"
            url = driver.current_url
            try:
                element = wait.until(EC.presence_of_element_located(login_button_locator))
                
                if element.is_displayed():
                    element.click()
                    
                    try:
                        fail_obj = wait.until(EC.presence_of_element_located(fail_cont))
                        fail_cta = driver.find_element(By.XPATH, global_variable.cta_fail).get_attribute("textContent")
                        #print(fail_cta)
                        assert fail_cta == cta_text, f"Expected is '{cta_text}' while the Actual is '{fail_cta}'"

                    except NoSuchElementException:
                        print("No such element found!")
                        return False
                    
                    except AssertionError:
                        print("Unmatched CTA text")
                        return False
                    
                    else:
                        if fail_obj.is_displayed() and url == exp_url:
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
                
        else:
            print(f"Step [{count_check}] input '{val}' as {element_input} is Failed ✘")
            return False
           
    except Exception as e:
        print(f"Can't handle the process! : {e}")
        return False

def run_test():
    print("Test Started...")
    step_results = False
    
    # ONE STEP CHECK
    print("=======================================================")
    step_results = input_check(username_locator, user_val)

    # Check overall test result
    if(step_results == True):
        print("Testcase - Empty Password, is running successfully!")
        print("=======================================================")
        driver.close()
        return True
    else:
        print('Testcase - Empty Password, is Failed!')
        print("=======================================================")
        driver.close()
        return False

# Call the main function if this script is executed

if __name__ == "__main__":
    run_test()