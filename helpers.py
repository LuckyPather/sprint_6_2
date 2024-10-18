from data import OrderData
from locators.order_page_locators import OrderCard

import random
import re
from faker import Faker


class Generator:
    def __init__(self):
        fake = Faker('ru_RU')
        self.name = fake.first_name()
        self.surname = fake.last_name()
        self.address = re.sub(r'[^a-zA-Zа-яА-Я0-9\s,\.]', '', fake.address())
        self.metro_station = random.randint(1, 5)
        self.phone_number = random.choice(OrderData.phone_numbers)
        self.data = fake.date_this_month().strftime('%d.%m.%Y')
        self.option_term = random.choice(OrderData.option_term)
        self.colors = random.choice([OrderCard.COLOR_BLACK, OrderCard.COLOR_GREY])
        self.comment = fake.sentence()
