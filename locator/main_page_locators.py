from selenium.webdriver.common.by import By

class MainPageLocators:
    #Логотипы "Самокат", "Яндекс"
    scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")
    yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")
    