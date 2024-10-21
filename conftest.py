from selenium import webdriver

import pytest
import logging


def pytest_configure(config):
    # Настраиваем логирование с уровнем INFO
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Удаляем все существующие обработчики pytest для избежания дублирования
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Устанавливаем уровень логов для CLI в pytest (выводится в реальном времени)
    config.option.log_cli = True
    config.option.log_cli_level = 'INFO'


@pytest.fixture
def connection():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
