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
    String loginLocator = global_variable.login_button;
    String nextUrl = global_variable.atc_url;

    WebDriver driver = new FirefoxDriver();
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(3));

    public static void main(String[] args) {
        test_check_login tcl = new test_check_login();

        for (String username : tcl.unameList){
            Boolean loginResult = check_richeck(tcl.usernameLocator, tcl.passwordLocator, username, tcl.passwVal);

            if (loginResult){
                System.out.println("Sukses" + username);
            }
            else {
                System.out.println("Failed" + username);
            }
        }
    }

    public static Boolean check_richeck(String username, String password, String uval, String pval){
        test_check_login tcl = new test_check_login();
        tcl.driver.get("https://saucedemo.com");
        Boolean result = false;
        try {
            WebElement uname = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(username)));
            WebElement passw = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(password)));
            WebElement userv = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(uval)));
            WebElement passv = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(pval)));
            WebElement login = tcl.wait.until(ExpectedConditions.presenceOfElementLocated(By.id(tcl.loginLocator)));
            if (uname.isDisplayed() && passw.isDisplayed()){
                System.out.println("Try login using : "+ userv + uval + pval);
                uname.sendKeys(uval);
                passw.sendKeys(pval);
                login.click();

                String thisUrl = tcl.driver.getCurrentUrl();

                if (thisUrl == tcl.nextUrl){
                    System.out.println("Url Expected, Finish with succeed!");
                    result = true;
                }
                else{
                    System.out.println("Url is not same, Finish with error!");
                    result = false;
                }
            }
        }
        catch (TimeoutException e){
            System.out.println("Timeout!");
            result = false;
        }
        finally {
            tcl.driver.quit();
        }

        if (result == true){
            System.out.println("Sukses");
            return true;
        }
        else {
            System.out.println("Failed");
            return false;
        }
    }
}
