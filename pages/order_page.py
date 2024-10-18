# Todo: тут я должен создать метод, который принимает тип кнопки заказать, заполняет ордер потом в тесте я проверяю сообщение
import time

import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderCard


class OrderPage(BasePage):
    @allure.step("Заполняю форму заказа")
    def create_order(self, name, surname, address, metro_station, phone_number, option_term, locator_for_colors,
                     comment):
        self.accept_cookie()
        self.click_to_element(OrderCard.BUTTON_GET_ORDER)
        self.send_keys(OrderCard.NAME, name)
        self.send_keys(OrderCard.SURNAME, surname)
        self.send_keys(OrderCard.ADDRESS, address)
        self.click_to_element(OrderCard.METRO_STATION)
        self.find_elements_with_wait(OrderCard.METRO_STATION_LIST)[metro_station].click()
        self.send_keys(OrderCard.PHONE_NUMBER, phone_number)
        self.click_to_element(OrderCard.BUTTON_NEXT)
        self.click_to_element(OrderCard.DATA)
        self.send_keys(OrderCard.DATA_DAY, Keys.ENTER)
        # Задаем срок аренды
        self.click_to_element(OrderCard.LEASE_PERIOD_ROW)
        options = self.find_elements_with_wait(OrderCard.LEASE_PERIOD_DROPDOWN_OPTION)
        for option in options:
            if option.text == option_term:
                option.click()
                break
        self.click_to_element(locator_for_colors)
        self.send_keys(OrderCard.COMMENT, comment)
        self.click_to_element(OrderCard.BUTTON_GET_ORDER)
        self.click_to_element(OrderCard.BUTTON_YES)
