import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url


class OtherFunction(BasePage):
    @allure.step("Нажимаю на кнопку Яндекс")
    def redirect_to_yandex(self):
        self.click_to_element(MainPageLocators.BUTTON_REDIRECT_TO_YANDEX_DZEN)
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == Url.YANDEX_DZEN_URL)
        url = self.driver.current_url
        number_tabs = len(self.driver.window_handles)
        return url, number_tabs

    @allure.step("Нажимаю на кнопку Самокат")
    def return_to_main_page(self):
        self.click_to_element(MainPageLocators.BUTTON_RETURN_TO_MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == Url.MAIN_PAGE_URL)
        url = self.driver.current_url
        return url
