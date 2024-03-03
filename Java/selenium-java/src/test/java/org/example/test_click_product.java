package org.example;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
public class test_click_product {
    private String passwVal = global_variable.password_val;
    private String userVal = global_variable.username_one;
    private String usernameLocator = global_variable.username;
    private String passwordLocator = global_variable.password;
    private String loginLocator = global_variable.login_button;
    private String ClickProduct = global_variable.product;
    private WebDriver driver;
    private WebDriverWait wait;

    public test_click_product(){
        driver = new FirefoxDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(3));
    }

    public static void main(String[] args) {
        test_click_product tcp = new test_click_product();
        tcp.click_product();
    }

    public Boolean click_product(){
        Boolean result = false;
        driver.get("https://saucedemo.com");

        try {
            WebElement uname = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(usernameLocator)));
            WebElement passw = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(passwordLocator)));
            WebElement login = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(loginLocator)));

            uname.sendKeys(userVal);
            passw.sendKeys(passwVal);
            login.click();

            WebElement product = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(ClickProduct)));
            JavascriptExecutor exec = (JavascriptExecutor) driver;
            exec.executeScript("arguments[0].click()", product);

            String thisUrl = "https://www.saucedemo.com/inventory-item.html?id=4";

            String currentUrl = driver.getCurrentUrl();

            if (currentUrl.equals(thisUrl)){
                System.out.println("Url Expected, Finish with succeed!");
                result = true;
                }
            else {
                System.out.println("Url Not Expected, Finish with failed!");
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

