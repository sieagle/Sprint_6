import allure
from locator.home_page_locators import HomePageLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def open(self, url):
        self.driver.get(url)
    
    @allure.step('Принять соглашение куки')
    def accept_cookie(self):
        self.click_button(HomePageLocators.cookie_botton)

    @allure.step('Найти кнопку "Заказать" в хедере')
    def find_order_button(self):
        return self.find_and_wait_locator(HomePageLocators.header_order_button)

    @allure.step('Скролл до вопросов')
    def scroll_to_questions_list(self):
        self.scroll_to_locator(HomePageLocators.questions_title)

    @allure.step('Клик на кнопку с вопросом')
    def click_question_button(self, locator):
        self.click_button(locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, text):
        self.find_and_wait_locator(HomePageLocators.question_buttons)
        text_question = self.get_text_locator(HomePageLocators.question_text_locator, text)
        return text_question

    @allure.step('Получение текста ответа')
    def get_text_answers(self, question_button_locator, question_text_locator):
        self.scroll_to_questions_list()
        self.click_question_button(question_button_locator)
        text_answer = self.find_and_wait_locator(question_text_locator).text
        return text_answer
    
    @allure.step('Скролл до нижней кнопки "Заказать"')
    def scroll_to_bottom_order_button(self):
        return self.scroll_to_locator(HomePageLocators.bottom_order_button)

    @allure.step('Клик по нижней кнопке "Заказать"')
    def scroll_and_click_order_button(self):
        self.scroll_to_locator(HomePageLocators.bottom_order_button)
        self.click_button(HomePageLocators.bottom_order_button)
