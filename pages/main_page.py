from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locator.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()
    
    def send_keys(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)
    
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text
    
    def is_text_equals(self, locator, text):
        return self.get_text_locator(locator) == text
    
    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()
    
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    def yandex_logo_click(self):
        self.click_button(MainPageLocators.yandex_logo)

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def scooter_logo_click(self):
        self.click_button(MainPageLocators.scooter_logo)