
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators


class TestSwitchToPersonalAccount:

    #Тест перехода в Личный кабинет
    def test_switch_to_personal_account(self, driver):

        driver.get(data.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.TAG_NAME, "button")))
        driver.find_element(By.XPATH, locators.login_button_on_mane_page).click()
        driver.find_element(By.XPATH, locators.login_email_input).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, locators.login_password_input).send_keys(data.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, locators.login_button)))
        driver.find_element(By.CSS_SELECTOR, locators.login_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")))
        element = driver.find_element(By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
        assert element.text == "В этом разделе вы можете изменить свои персональные данные"
        driver.quit()




