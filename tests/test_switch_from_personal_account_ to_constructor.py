
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestSwitchFromPersonalAccountToConstructor:

    #Тест перехода из личного кабинета в коснтруктор
    def test_switch_to_сonstructor_from_account(self, driver):

        driver.get(data.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_button_on_mane_page).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.login_button)))
        driver.find_element(By.XPATH, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, locators.personal_account_button)))
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.constructor_button).click()

        element = driver.find_element(By.CSS_SELECTOR, locators.element_on_main_page)
        assert element.is_displayed()


    # Тест перехода из личного кабинета в коснтруктор через логотип
    def test_switch_to_сonstructor_from_account_by_logo(self, driver):

            driver.get(data.URL_MAIN)

            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.TAG_NAME, "button")))
            driver.find_element(By.XPATH, locators.login_button_on_mane_page).click()
            driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
            driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
            WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, locators.login_button)))
            driver.find_element(By.XPATH, locators.login_button).click()
            WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, locators.personal_account_button)))
            driver.find_element(By.XPATH, locators.personal_account_button).click()
            driver.find_element(By.CSS_SELECTOR, locators.logo_button).click()

            element = driver.find_element(By.CSS_SELECTOR, locators.element_on_main_page)

            assert element.is_displayed()
