from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вопрос - ответ
    QUESTION_UNIVERSAL_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_UNIVERSAL_LOCATOR = By.ID, 'accordion__panel-{}'
    # Последний вопрос для скрола
    QUESTION_8 = By.ID, 'accordion__heading-7'
    # Кнопка принятия куки
    ACCEPT_COOKIE_BUTTON_UPPER = By.ID, 'rcc-confirm-button'
    # Кнопки перехода и редирект
    BUTTON_RETURN_TO_MAIN_PAGE = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    BUTTON_REDIRECT_TO_YANDEX_DZEN = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
