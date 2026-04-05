from pages.main_page import MainPage
from locator.dzen_page_locators import DzenPageLocator
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DzenPage(MainPage):
    
    @allure.step('Отображение кнопки "Главная" на странице Дзен')
    def check_elements(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(DzenPageLocator.dzen_main_button))