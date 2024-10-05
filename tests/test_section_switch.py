from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestSectionSwitch:

    #Тест выхода из аккаунта
    def test_section_switch(self, driver):

        driver.get(data.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_button_on_mane_page).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, locators.login_button)))
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, locators.bread_button)))
        driver.find_element(By.CSS_SELECTOR, locators.source_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Соусы')]")))
        element = driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]")
        assert element.text == "Соусы"
        driver.find_element(By.CSS_SELECTOR, locators.bread_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Булки')]")))
        element = driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]")
        assert element.text == "Булки"
        driver.find_element(By.CSS_SELECTOR, locators.topping_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Начинки')]")))
        element = driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]")
        assert element.text == "Начинки"
        driver.quit()