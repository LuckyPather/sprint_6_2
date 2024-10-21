from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.find_element_with_wait(locator).send_keys(value)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def accept_cookie(self):
        self.click_to_element(MainPageLocators.ACCEPT_COOKIE_BUTTON_UPPER)

    def redirect_get_handles(self, locator, number):
        self.click_to_element(locator)
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > number)
        number_tabs = len(self.driver.window_handles)
        return number_tabs

    def switch_to_window_and_get_url(self, number, url):
        self.driver.switch_to.window(self.driver.window_handles[number])
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url)
        url = self.driver.current_url
        return url