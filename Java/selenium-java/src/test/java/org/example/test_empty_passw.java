package org.example;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
public class test_empty_passw {
    private String userVal = global_variable.username_one;
    private String usernameLocator = global_variable.username;
    private String passwordLocator = global_variable.password;
    private String loginLocator = global_variable.login_button;
    private String fail_container = global_variable.fail_container;
    private WebDriver driver;
    private WebDriverWait wait;
    private String cta_text = "Epic sadface: Password is required";

    public test_empty_passw(){
        driver = new FirefoxDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(3));
    }

    public static void main(String[] args) {
        test_empty_passw tep = new test_empty_passw();
        tep.empty_passw();
    }

    public Boolean empty_passw(){
        Boolean result = false;
        driver.get("https://saucedemo.com");

        try {
            WebElement uname = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(usernameLocator)));
            WebElement login = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(loginLocator)));

            String thisUrl = driver.getCurrentUrl();
            uname.sendKeys(userVal);
            login.click();

            WebElement fail_cont = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(fail_container)));
            String cont_cta = fail_cont.getAttribute("textContent");
            Boolean assertionResult = cont_cta.equals(cta_text);
            // String res = assertionResult.toString();
            if (assertionResult){
                System.out.println("Fail happen as expected, success!");
                result = true;
            }
            else {
                System.out.println("Fail not happen as expected, failed!");
                result = false;
            }
        } catch (TimeoutException e) {
            System.out.println("Timeout!");
            result = false;
        }
        driver.quit();
        return result;
    }
}

