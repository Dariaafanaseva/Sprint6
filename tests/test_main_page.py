import allure
import pytest
from data import ANSWER_TEXTS
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @allure.description(
        'Проверяем, что при клике на вопрос, ответ правильный')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_TEXTS[0]),
            (1, ANSWER_TEXTS[1]),
            (2, ANSWER_TEXTS[2]),
            (3, ANSWER_TEXTS[3]),
            (4, ANSWER_TEXTS[4]),
            (5, ANSWER_TEXTS[5]),
            (6, ANSWER_TEXTS[6]),
            (7, ANSWER_TEXTS[7])
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.get(("https://qa-scooter.praktikum-services.ru/"))
        main_page.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        assert main_page.get_answer_text(num) == result

