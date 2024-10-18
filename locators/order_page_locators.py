from selenium.webdriver.common.by import By


class OrderCard:
    UPPER_BUTTON_GET_ORDER = By.XPATH, ("//*[@class='Button_Button__ra12g' and text("
                                        ")='Заказать']")
    # Карточка заказа
    NAME = By.XPATH, "//*[@placeholder = '* Имя']"
    SURNAME = By.XPATH, "//*[@placeholder = '* Фамилия']"
    ADDRESS = By.XPATH, "//*[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//*[@placeholder = '* Станция метро']"
    METRO_STATION_LIST = By.XPATH, "//*[@class = 'select-search__row']"
    PHONE_NUMBER = By.XPATH, "//*[@placeholder = '* Телефон: на него позвонит курьер']"

    BUTTON_NEXT = By.XPATH, "//*[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']"

    # Карточка аренды
    DATA = By.XPATH, "//*[@placeholder = '* Когда привезти самокат']"
    DATA_DAY = By.CSS_SELECTOR, ".react-datepicker__day--017"
    LEASE_PERIOD_ROW = By.XPATH, "//*[@class = 'Dropdown-placeholder' and text()='* Срок аренды']"  # Нажимаем чтобы появился следующий элемент
    LEASE_PERIOD_DROPDOWN_OPTION = By.XPATH, "//div[@class='Dropdown-option']"  # Опция, искать будем по совпадению текста
    # Цвет самоката
    COLOR_BLACK = By.ID, "black"
    COLOR_GREY = By.ID, "grey"
    # Комментарий
    COMMENT = By.XPATH, "//*[@placeholder = 'Комментарий для курьера']"
    BUTTON_GET_ORDER = By.XPATH, "//*[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    # Кнопка ДА
    BUTTON_YES = By.XPATH, ".//button[text()='Да']"
    SUCCESS_MESSAGE = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
