package org.example;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
public class test_ver_elem {
    private String usernameLocator = global_variable.username;
    private String passwordLocator = global_variable.password;
    private String loginLocator = global_variable.login_button;
    private String credentialLocator = global_variable.uname_credential;
    private String credentialPassLocator = global_variable.pass_credential;
    private String titleLocator = global_variable.title;
    private String titleTxt = "Swag Labs";
    private WebDriver driver;
    private WebDriverWait wait;

    public test_ver_elem(){
        driver = new FirefoxDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(3));
    }

    public static void main(String[] args) {
        test_ver_elem tve = new test_ver_elem();
        tve.ver_elem();
    }

    public Boolean ver_elem(){

        Boolean result = false;
        driver.get("https://saucedemo.com");

        try {
            WebElement uname = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(usernameLocator)));
            WebElement passw = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(passwordLocator)));
            WebElement login = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(loginLocator)));
            WebElement cred = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(credentialLocator)));
            WebElement passcred = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(credentialPassLocator)));
            WebElement title = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(titleLocator)));

            String titleText = title.getAttribute("textContent");
            Boolean assertionResult = titleText.equals(titleTxt);

            if (uname.isDisplayed() && passw.isDisplayed() && login.isDisplayed() && cred.isDisplayed() && passcred.isDisplayed() && title.isDisplayed()){
                System.out.println("Success validate the components");
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

