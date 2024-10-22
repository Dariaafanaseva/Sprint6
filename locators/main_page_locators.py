from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = By.ID, "rcc-confirm-button"
    MAKE_ORDER_BUTTON_ON_HEADER = By.XPATH, '//div[2]/button[contains(text(),"Заказать")]'
    MAKE_ORDER_BUTTON_ON_DOWN = By.XPATH, '//div[5]/button[contains(text(),"Заказать")]'
    TITLE_QUESTIONS = By.XPATH, '//div[contains(text(),"Вопросы о важном")]'
    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]' 
    LAST_QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-7"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]'
