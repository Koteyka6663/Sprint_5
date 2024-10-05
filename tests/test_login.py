
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_on_the_main_page(self, driver):

        driver.get(data.URL_MAIN)

        driver.find_element(By.XPATH, locators.login_button_on_mane_page).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, locators.login_button)))
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, locators.main_heading)))
        element = driver.find_element(By.CSS_SELECTOR, locators.main_heading)
        assert element.text == "Соберите бургер"

        driver.quit()

    # вход через кнопку «Личный кабинет»,
    def test_login_on_the_main_page_header_button(self, driver):

        driver.get(data.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_header_button).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, locators.main_heading)))
        element = driver.find_element(By.CSS_SELECTOR, locators.main_heading)
        assert element.text == "Соберите бургер"

        driver.quit()

    # вход через кнопку в форме регистрации
    def test_login_on_the_registration_page(self, driver):

        driver.get(data.URL_REGISTRATION)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_button_in_registration).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, locators.main_heading)))
        element = driver.find_element(By.CSS_SELECTOR, locators.main_heading)
        assert element.text == "Соберите бургер"

        driver.quit()

    # вход через кнопку в форме восстановления пароля
    def test_login_on_the_forgot_password_page(self, driver):

        driver.get(data.URL_FORGOT_PASSWORD)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_button_in_forgot_password).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, locators.main_heading)))
        element = driver.find_element(By.CSS_SELECTOR, locators.main_heading)
        assert element.text == "Соберите бургер"

        driver.quit()
