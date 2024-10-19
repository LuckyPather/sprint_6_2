from pages.order_page import OrderPage
from locators.order_page_locators import OrderCard
from data import Url
from helpers import Generator
import allure
import pytest


@pytest.mark.order_page
@allure.suite("Страница заказа")
@allure.sub_suite("Заказ")
class TestOrderPage:
    @allure.title("Оформление заказа")
    @allure.description("Проверяю оформление заказа")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('button', [OrderCard.UPPER_BUTTON_GET_ORDER, OrderCard.DOWN_BUTTON_GET_ORDER])
    def test_create_order(self, connection, button):
        order_page = OrderPage(connection)
        generator = Generator()
        with allure.step("Проверяю загрузку страницы"):
            connection.get(Url.MAIN_PAGE_URL)
        with allure.step(f"Перехожу на страницу заказа в зависимости от переданого локатора {button}, заполняю "
                         f"карточку заказа"):
            order_page.create_order(button, generator.name, generator.surname, generator.address,
                                    generator.metro_station,
                                    generator.phone_number, generator.option_term,
                                    generator.colors, generator.comment)

            assert "Заказ оформлен" in order_page.get_text_from_element(OrderCard.SUCCESS_MESSAGE), "Проверка не прошла"
