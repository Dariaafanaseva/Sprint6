import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Переходим на страницу самоката')
    def get(self, url):
        self.driver.get(url)
    @allure.step('Кликаем на вопрос')
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст с ответа')
    def get_answer_text_1(self, locator_a_formatted):
        return self.get_text_from_element(locator_a_formatted)

    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_question(locator_q_formatted)
        return self.get_answer_text_1(locator_a_formatted)

