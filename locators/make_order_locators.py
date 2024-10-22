from selenium.webdriver.common.by import By


class MakeOrderLocators:

    NAME_INPUT_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_INPUT_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_INPUT_FIELD = By.XPATH, '//input[@placeholder="* Станция метро"]'
    METRO_STATION_OPTION = By.XPATH, '//ul/li[1]' #станция метро Бульвар Рокосовского
    TELEPHONE_NUMBER = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[contains(text(),"Далее")]'
    ABOUT_RENT_HEADER = By.XPATH, '//div[contains(text(),"Про аренду")]'
    DELIVERY_DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_ARROW = By.XPATH, '//span[@class="Dropdown-arrow"]'
    RENTAL_PERIOD_TWO_DAYS = By.XPATH, '//div[@class="Dropdown-option"][2]'
    SCOOTER_COLOR = By.XPATH,  '//div[contains(text(),"Цвет самоката")]/parent::div'
    MAKE_ORDER_BUTTON = By.XPATH, '//div[3]/button[contains(text(),"Заказать")]'
    YES_BUTTON = By.XPATH, '//button[contains(text(),"Да")]'
    POPUP_ORDER_PLACED_BUTTON = By.XPATH, '//div/button[contains(text(),"Посмотреть статус")]'



