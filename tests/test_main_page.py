import allure
import pytest

from pages.main_page import MainPage
from data import AnswerText, QuestionText, Url


@allure.suite("Главная страница")
@allure.sub_suite("Меню вопросов и ответов")
class TestMainPage:

    @allure.description('Проверяем соответствие ожидаемых названий вопросов и ответов с фактическими, а также '
                        'корректность их соотношения')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num, question_text, answer_text',
                             [
                                 (0, QuestionText.QUESTION_1, AnswerText.ANSWER_1),
                                 (1, QuestionText.QUESTION_2, AnswerText.ANSWER_2),
                                 (2, QuestionText.QUESTION_3, AnswerText.ANSWER_3),
                                 (3, QuestionText.QUESTION_4, AnswerText.ANSWER_4),
                                 (4, QuestionText.QUESTION_5, AnswerText.ANSWER_5),
                                 (5, QuestionText.QUESTION_6, AnswerText.ANSWER_6),
                                 (6, QuestionText.QUESTION_7, AnswerText.ANSWER_7),
                                 (7, QuestionText.QUESTION_8, AnswerText.ANSWER_8)
                             ]
                             )
    def test_question_and_answers(self, connection, num, question_text, answer_text):
        allure.dynamic.title(f'Вопрос-ответ {num + 1}')
        with allure.step("Проверяю загрузку страницы"):
            connection.get(Url.MAIN_PAGE_URL)
        main_page = MainPage(connection)
        with allure.step(f"Проверяю текст вопроса и ответа под номером {num + 1}"):
            question, answer = main_page.get_answer_and_question_text(num)
            assert question == question_text, f"Ожидалось: {question_text}, получено: {question}"
            assert answer == answer_text, f"Ожидалось: {answer_text}, получено: {answer}"
