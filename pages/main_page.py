import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def get_answer_and_question_text(self, num):
        # Создаю локаторы для элементов, в зависимости от номера
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_UNIVERSAL_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_UNIVERSAL_LOCATOR, num)
        self.accept_cookie()
        # Прокручиваю для лучшей видимости к последнему элементу
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        # Нажимаю на вопрос, чтобы открыть ответ
        self.click_to_element(locator_q_formatted)
        # Получаю текст вопроса и ответа
        with allure.step(f"Получаю текст вопроса {self.get_text_from_element(locator_q_formatted)}"):
            question_text = self.get_text_from_element(locator_q_formatted)
        with allure.step(f"Получаю текст ответа {self.get_text_from_element(locator_a_formatted)}"):
            answer_text = self.get_text_from_element(locator_a_formatted)
        return question_text, answer_text
