
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestSectionSwitch:

    #Тест перехода во второй раздел конструктора
    def test_second_section_switch(self, driver):

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
            (By.XPATH, locators.source_button)))
        driver.find_element(By.XPATH, locators.source_button).click()

        element = driver.find_element(By.XPATH, locators.current_element)
        element2 = driver.find_element(By.XPATH, locators.source_button)

        assert element == element2


    # Тест перехода в первый раздел конструктора
    def test_first_section_switch(self, driver):

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
            (By.XPATH, locators.bread_button)))
        driver.find_element(By.XPATH, locators.source_button).click()
        driver.find_element(By.XPATH, locators.bread_button).click()

        element = driver.find_element(By.XPATH, locators.current_element)
        element2 = driver.find_element(By.XPATH, locators.bread_button)
        assert element == element2


    # Тест перехода в третий раздел конструктора
    def test_third_section_switch(self, driver):
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
            (By.XPATH, locators.topping_button)))
        driver.find_element(By.XPATH, locators.topping_button).click()

        element = driver.find_element(By.XPATH, locators.current_element)
        element2 = driver.find_element(By.XPATH, locators.topping_button)

        assert element == element2
