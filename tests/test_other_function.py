import allure
from pages.other_function import OtherFunction
from data import Url


@allure.suite("Другие функции")
@allure.sub_suite("Редирект и переход")
@allure.description('Проверяем кнопки редиректа и перехода с главного окна')
@allure.severity(allure.severity_level.NORMAL)
class TestOtherFunction:
    @allure.title("Редирект на страницу Яндекс Дзен")
    def test_redirect_to_yandex_dzen(self, connection):
        other_function = OtherFunction(connection)
        with allure.step("Проверяю загрузку основной страницы"):
            connection.get(Url.MAIN_PAGE_URL)
        with allure.step("Проверяю перенаправление на Яндекс Дзен"):
            url, number_tabs = other_function.redirect_to_yandex()
            assert url == Url.YANDEX_DZEN_URL, f"Ожидалось {Url.YANDEX_DZEN_URL}, получено: {url}"
            assert number_tabs == 2, f"Ожидалось количество вкладок 2, получено {number_tabs}"

    @allure.title("Переход на главную страницу")
    def test_return_to_home_page(self, connection):
        other_function = OtherFunction(connection)
        with allure.step("Проверяю загрузку страницы заказа"):
            connection.get(Url.ORDER_PAGE_URL)
        with allure.step("Проверяю переход на домашнюю страницу"):
            url = other_function.return_to_main_page()
            assert url == Url.MAIN_PAGE_URL, f"Ошибка перехода, ожидалось {Url.MAIN_PAGE_URL} получено: {url}"
