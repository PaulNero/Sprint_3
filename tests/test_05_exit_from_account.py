import pytest

from src import data
from src import links
from src import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.all
@pytest.mark.exit
def test_exit_private_cabinet_chrome_success(driver):
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_email_for_login)).send_keys(data.email_for_login)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.input_password)).send_keys(data.password_right)
        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_complite_login)).click()
        WebDriverWait(driver, data.delay).until(EC.url_to_be(links.main_link))

        assert driver.current_url == links.main_link

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_open_private_cabinet)).click()
        WebDriverWait(driver, data.delay).until(
            EC.url_contains(links.private_cabinet))

        assert driver.current_url == links.main_link + links.private_cabinet

        WebDriverWait(driver, data.delay).until(
            EC.element_to_be_clickable(locators.button_exit_from_account)).click()
        WebDriverWait(driver, data.delay).until(
            EC.url_contains(links.login_link))

        assert driver.current_url == links.main_link + links.login_link
