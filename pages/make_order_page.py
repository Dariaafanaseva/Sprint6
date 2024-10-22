import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.make_order_locators import MakeOrderLocators


class OrderPage(BasePage):
    @allure.step('Переходим на страницу самоката')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Создаем заказ с кнопкой "Заказать" вверху станицы')
    def make_order_button_on_header(self, name, surname, address, telephone):
        self.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        self.find_element_with_wait(MainPageLocators.MAKE_ORDER_BUTTON_ON_HEADER).click()
        self.add_text_to_element(MakeOrderLocators.NAME_INPUT_FIELD, name)
        self.add_text_to_element(MakeOrderLocators.SURNAME_INPUT_FIELD, surname)
        self.add_text_to_element(MakeOrderLocators.ADDRESS_INPUT_FIELD, address)
        self.click_to_element(MakeOrderLocators.METRO_INPUT_FIELD)
        self.find_element_with_wait(MakeOrderLocators.METRO_STATION_OPTION).click()
        self.add_text_to_element(MakeOrderLocators.TELEPHONE_NUMBER, telephone)
        self.click_to_element(MakeOrderLocators.NEXT_BUTTON)
        self.find_element_with_wait(MakeOrderLocators.ABOUT_RENT_HEADER)
        self.click_to_element(MakeOrderLocators.DELIVERY_DATE)
        self.add_text_to_element(MakeOrderLocators.DELIVERY_DATE, '25.10.2024')
        self.click_to_element(MakeOrderLocators.RENTAL_PERIOD_ARROW)
        self.click_to_element(MakeOrderLocators.RENTAL_PERIOD_TWO_DAYS)
        self.click_to_element(MakeOrderLocators.MAKE_ORDER_BUTTON)
        self.find_element_with_wait(MakeOrderLocators.YES_BUTTON).click()

    @allure.step('Создаем заказ с кнопкой "Заказать" внизу станицы')
    def make_order_button_on_down(self, name, surname, address, telephone):
        self.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        self.scroll_to_element(MainPageLocators.TITLE_QUESTIONS)
        self.find_element_with_wait(MainPageLocators.MAKE_ORDER_BUTTON_ON_DOWN).click()
        self.add_text_to_element(MakeOrderLocators.NAME_INPUT_FIELD, name)
        self.add_text_to_element(MakeOrderLocators.SURNAME_INPUT_FIELD, surname)
        self.add_text_to_element(MakeOrderLocators.ADDRESS_INPUT_FIELD, address)
        self.click_to_element(MakeOrderLocators.METRO_INPUT_FIELD)
        self.find_element_with_wait(MakeOrderLocators.METRO_STATION_OPTION).click()
        self.add_text_to_element(MakeOrderLocators.TELEPHONE_NUMBER, telephone)
        self.click_to_element(MakeOrderLocators.NEXT_BUTTON)
        self.find_element_with_wait(MakeOrderLocators.ABOUT_RENT_HEADER)
        self.click_to_element(MakeOrderLocators.DELIVERY_DATE)
        self.add_text_to_element(MakeOrderLocators.DELIVERY_DATE, '25.10.2024')
        self.click_to_element(MakeOrderLocators.RENTAL_PERIOD_ARROW)
        self.click_to_element(MakeOrderLocators.RENTAL_PERIOD_TWO_DAYS)
        self.click_to_element(MakeOrderLocators.MAKE_ORDER_BUTTON)
        self.find_element_with_wait(MakeOrderLocators.YES_BUTTON).click()


    @allure.step('Проверяем, что заказ создался')
    def check_order(self):
        return self.get_text_from_element(MakeOrderLocators.POPUP_ORDER_PLACED_BUTTON)
