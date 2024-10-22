import allure
from pages.base_page import BasePage
from locators.switch_locators import SwitchToPageLocators
from locators.main_page_locators import MainPageLocators

class SwitchToPage(BasePage):
    @allure.step('Переходим на страницу самоката')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Переходим на страницу самоката, при нажатии на лого самоката')
    def switch_to_scooter_main_page(self):
        self.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON_ON_HEADER)
        self.find_element_with_wait(SwitchToPageLocators.HEADER_LOGO_SCOOTER).click()

    @allure.step('Переходим на страницу Дзена, при нажатии на лого Яндекс')
    def switch_to_dzen(self):
        self.accept_cookies(MainPageLocators.COOKIE_BUTTON)
        self.find_element_with_wait(SwitchToPageLocators.HEADER_LOGO_YANDEX).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.find_element_with_wait(SwitchToPageLocators.DZEN_SEARCH_BAR_BUTTON)





