from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append('C:/Users/ringgo.atmojo/Documents/GitRepository/Selenium/Saucedemo')
import global_variable

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver, 5)

username_locator = (By.ID, global_variable.username)
password_locator = (By.ID, global_variable.password)
login_button_locator = (By.XPATH, global_variable.login_button)
product = (By.XPATH, global_variable.product)

user_val = global_variable.username_one 
pass_val = global_variable.password_val

count_check = 0

def skip_steps(element_input, val):
    try:
        attr = wait.until(EC.presence_of_element_located(element_input))

        if attr.is_displayed():
            attr.send_keys(val)
            attr.send_keys(Keys.RETURN)
            print(f"Input {element_input}...")
            return True
        
        else:
            print(f"Input {element_input} failed.")
            return False
           
    except Exception as e:
        print(f"Can't handle the process!")
        return False

def skip_login():
    exp_url = "https://www.saucedemo.com/inventory.html"
    try:
        element = wait.until(EC.presence_of_element_located(login_button_locator))
        
        if element.is_displayed():
            print("Element displayed")
            element.click()

            url = driver.current_url

            if url == exp_url:
                print(f"Click login button...")
                return True
            
            else:
                print(f"Click login button failed.")
                return False
    
        else:
            print("Can't handle the process!")
            return False
        
    except NoSuchElementException:
        print("Element not Found!")
        return False

def getElementText():
    element_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    
    try:
        element = wait.until(EC.presence_of_element_located(product))
        
        if element.is_displayed():
            driver.execute_script("arguments[0].click();",element)
            url = driver.current_url

            if url == element_url:
                print(f"Click product...")
                return True
            else:
                print(f"Click product failed.")
                return False
        else:
            print("Can't handle the process!")
            return False
        
    except NoSuchElementException:
        print("Element not Found!")
        return False



def run_test():
    print("Test Started...")
    step_results = [False] * 4
    
    # USERNAME
    print("=======================================================")
    step_results[0] = skip_steps(username_locator, user_val)

    # PASSWORD
    step_results[1] = skip_steps(password_locator, pass_val)

    # CLICK LOGIN
    step_results[2] = skip_login()

    #CLICK PRODUCT
    step_results[3] = getElementText()

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