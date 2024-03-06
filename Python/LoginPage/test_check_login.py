from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append('C:/Users/Admin/Documents/selenium/Python')
import global_variable

driver = webdriver.Firefox()
new_url = "https://www.saucedemo.com"
exp_url = "https://www.saucedemo.com/inventory.html"
wait = WebDriverWait(driver, 5)

username_locator = (By.ID, global_variable.username)
password_locator = (By.ID, global_variable.password)
login_button_locator = (By.XPATH, global_variable.login_button)

uname_list = [global_variable.username_one, 
              #global_variable.username_two, been locked out
              global_variable.username_three,
              global_variable.username_four,
              global_variable.username_five,
              global_variable.username_six]

passw_val = global_variable.password_val

count = 0

def check_and_direct(username, password, uval, pval):
    global count
    count += 1
    try:
        driver.get(new_url)
        uname = wait.until(EC.presence_of_element_located(username))
        passw = wait.until(EC.presence_of_element_located(password))
        login = wait.until(EC.element_to_be_clickable(login_button_locator))

        if uname.is_displayed and passw.is_displayed():
            uname.send_keys(uval, Keys.RETURN)
            passw.send_keys(pval, Keys.RETURN)

            print(f"{count} Try login using {uval} and {pval}...")
            login.click()

            get_url = driver.current_url

            if get_url == exp_url:
                print(f"Directed to Expected URL, Login Succeed!")
                print("------------")
                return True
            
            else:
                print("Error when click on the button, Login Failed!")
                print("------------")
                return False
        
        else:
            print("An error occured!")
            print("------------")
            return False

    except NoSuchElementException as e:
        print(f"No such element found")
        print("------------")
        return False
     
    except Exception as e:
        print(f"Can't handle the process!")
        print("------------")
        return False

def run_test():
    print("Test Started...")
    step_results = [False] * 5
    
    #1
    print("=======================================================")
    #step_results[0] = check_and_direct(username_locator, password_locator, uname_list[0], passw_val)

    #2
    #step_results[1] = check_and_direct(username_locator, password_locator, uname_list[1], passw_val)

    #3
    #step_results[2] = check_and_direct(username_locator, password_locator, uname_list[2], passw_val)

    #4
    #step_results[3] = check_and_direct(username_locator, password_locator, uname_list[3], passw_val)

    #5
    #step_results[4] = check_and_direct(username_locator, password_locator, uname_list[4], passw_val)

    for index, username in enumerate(uname_list):
        step_results[index] = check_and_direct(username_locator, password_locator, username, passw_val)

    #step_results_bool = [bool(result) for result in step_results]

    # Check overall test result
    if all(step_results):
        print("Testcase - Login, is running successfully!")
        print("=======================================================")
        driver.close()
        return True
    else:
        print('Testcase - Login, is Failed!')
        print("=======================================================")
        driver.close()
        return False

# Call the main function if this script is executed

if __name__ == "__main__":
    run_test()