from selenium.webdriver.common.by import By


class SwitchToPageLocators:
    HEADER_LOGO_SCOOTER = By.XPATH, '//img[@alt="Scooter"]'
    HEADER_LOGO_YANDEX = By.XPATH, '//img[@alt="Yandex"]'
    DZEN_SEARCH_BAR_BUTTON = By.XPATH, '//button[@type="submit"]'