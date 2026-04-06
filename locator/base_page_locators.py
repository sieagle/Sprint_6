from selenium.webdriver.common.by import By

class BasePageLocators:
    #Логотипы "Самокат", "Яндекс"
    scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")
    yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")

    #Кнопка "главная" на главной странице "дзен"
    dzen_main_button = (By.XPATH, ".//span[text() = 'Главная']")
    