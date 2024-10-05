
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators
from tests import helper


class TestRegistration:

    #Тест регистрации пользователя
    def test_successfull_registration(self, driver):

        driver.get(data.URL_REGISTRATION)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.registration_name_input).send_keys(data.NAME)
        driver.find_element(By.XPATH, locators.registration_email_input).send_keys(helper.generate_email())
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys(helper.generate_password())
        driver.find_element(By.CSS_SELECTOR, locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.login_heading)))
        element = driver.find_element(By.XPATH, locators.login_heading)
        assert element.text == "Вход"

        driver.quit()

    #Тест наличия ошибки при некорректном пароле
    def test_wrong_password(self, driver):
        driver.get(data.URL_REGISTRATION)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.registration_name_input).send_keys(data.NAME)
        driver.find_element(By.XPATH, locators.registration_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys("1234")
        driver.find_element(By.CSS_SELECTOR, locators.registration_button).click()
        elem = driver.find_element(By.XPATH, locators.registration_password_error)
        assert elem.text == "Некорректный пароль"

        driver.quit()
