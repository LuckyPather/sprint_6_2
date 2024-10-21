import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url


class OtherFunction(BasePage):
    @allure.step("Нажимаю на кнопку Яндекс")
    def redirect_to_yandex(self):
        numbers_tabs = self.redirect_get_handles(MainPageLocators.BUTTON_REDIRECT_TO_YANDEX_DZEN, 1)
        url = self.switch_to_window_and_get_url(-1, Url.YANDEX_DZEN_URL)
        return numbers_tabs, url

    @allure.step("Нажимаю на кнопку Самокат")
    def return_to_main_page(self):
        self.redirect_get_handles(MainPageLocators.BUTTON_RETURN_TO_MAIN_PAGE, 0)
        url = self.switch_to_window_and_get_url(0, Url.MAIN_PAGE_URL)
        return url
