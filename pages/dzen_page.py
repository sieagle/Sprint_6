from locator.base_page_locators import BasePageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DzenPage(BasePage):
    
    @allure.step('Отображение кнопки "Главная" на странице Дзен')
    def check_elements(self):
        return self.wait_for_element(BasePageLocators.dzen_main_button)