from pages.switch_to_page import SwitchToPage
import allure

class TestSwitchTo:
    @allure.description(
        'Проверяем, что при клике на лого Самоката, происходит переход на главную страницу')
    def test_to_scooter_main_page(self, driver):
        switch_to_page = SwitchToPage(driver)
        switch_to_page.get(("https://qa-scooter.praktikum-services.ru/"))
        switch_to_page.switch_to_scooter_main_page()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description(
        'Проверяем, что при клике на лого Яндекс, происходит переход на Дзен')
    def test_to_dzen(self, driver):
        switch_to_page = SwitchToPage(driver)
        switch_to_page.get(("https://qa-scooter.praktikum-services.ru/"))
        switch_to_page.switch_to_dzen()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

