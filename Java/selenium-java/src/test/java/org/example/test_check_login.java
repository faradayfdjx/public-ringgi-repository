package org.example;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class test_check_login {
    String[] unameList = {
            global_variable.username_one,
            global_variable.username_three,
            global_variable.username_four,
            global_variable.username_five,
            global_variable.username_six
    };
    String passwVal = global_variable.password_val;
    String usernameLocator = global_variable.username;
    String passwordLocator = global_variable.password;
    Boolean result = false;

    WebDriver driver = new FirefoxDriver();
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(3));
    public static void main(String[] args) {
        check_richeck();
    }

    public static Boolean check_richeck(){
        test_check_login tcl = new test_check_login();
        tcl.driver.get("https://saucedemo.com");
        try {
            WebElement uname = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(tcl.usernameLocator)));
            if (uname.isDisplayed()){
                tcl.result = true;
            }
        }
        catch (NoSuchElementException e){
            System.out.println("No such element found!");
            tcl.result = false;
        }
        catch (TimeoutException e){
            System.out.println("Timeout!");
            tcl.result = false;
        }
        finally {
            tcl.driver.quit();
        }

        if (tcl.result == true){
            System.out.println("Sukses");
            return true;
        }
        else {
            System.out.println("Failed");
            return false;
        }
    }
}
