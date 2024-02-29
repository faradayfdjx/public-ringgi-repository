package org.example;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class test_check_login {
    private String[] unameList = {
            global_variable.username_one,
            global_variable.username_three,
            global_variable.username_four,
            global_variable.username_five,
            global_variable.username_six
    };

    private String passwVal = global_variable.password_val;
    private String usernameLocator = global_variable.username;
    private String passwordLocator = global_variable.password;
    private String loginLocator = global_variable.login_button;
    private String nextUrl = global_variable.atc_url;

    private WebDriver driver;
    private WebDriverWait wait;

    public test_check_login() {
        driver = new FirefoxDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(4));
    }

    public static void main(String[] args) {
        test_check_login tcl = new test_check_login();
        tcl.runTests();
    }

    public void runTests() {
        for (String username : unameList) {
            Boolean loginResult = check_richeck(username, passwVal);
            if (loginResult) {
                System.out.println("Sukses" + username);
            } else {
                System.out.println("Failed" + username);
            }
        }
        driver.quit();
    }

    public Boolean check_richeck(String uval, String pval) {
        driver.get("https://saucedemo.com");
        Boolean result = false;
        try {
            WebElement uname = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(usernameLocator)));
            WebElement passw = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(passwordLocator)));
            WebElement login = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(loginLocator)));

            if (uname.isDisplayed() && passw.isDisplayed()){
                System.out.println("Try login using : " + uval + " " + pval);
                uname.sendKeys(uval);
                passw.sendKeys(pval);
                login.click();

                String thisUrl = driver.getCurrentUrl();
                    if (thisUrl.equals(nextUrl)) {
                        System.out.println("Url Expected, Finish with succeed!");
                        result = true;
                    } else {
                        System.out.println("Url is not same, Finish with error!");
                        result = false;
                    }
            }
        } catch (TimeoutException e) {
            System.out.println("Timeout!");
            result = false;
        }
        return result;
    }
}
