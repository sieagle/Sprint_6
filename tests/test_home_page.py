import allure
import time
import pytest
from pages.main_page import MainPage
from pages.home_page import HomePage
from locator.home_page_locators import HomePageLocators
from dictionary.main_page_dictionary import Urls
from dictionary.home_page_dictionary import Questions
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage:
    @allure.title('Тест на проверку того, что на странице 2 кнопки заказать')
    @allure.description('1.Найти кнопку "Заказать" в хедере,' 
                        '2. Проскроллить страницу и найти кнопку "Заказать" в середине страницы')
    def test_two_buttons_in_page(self, driver):
        page = HomePage(driver)
        orderTopButton = page.find_order_button()
        EC._element_if_visible(orderTopButton)
        assert orderTopButton.is_displayed(), f"{orderTopButton} не отображается на странице"
        orderBottomButton = page.scroll_to_bottom_order_button()
        EC._element_if_visible(orderBottomButton)
        assert orderBottomButton.is_displayed(), f"{orderBottomButton} не отображается на странице"

    @allure.title('Тест для проверки текстов в ответах на вопросы о важном')
    @allure.description('1.Скролл до блока с вопросами'
                        '2. Клик на кнопку с вопросом'
                        '3. Получение текста ответа'
                        '4. Сравинть ОР и ФР')
    @pytest.mark.parametrize('question_buttons, answers_text_locator, expected_question_text', zip(HomePageLocators.question_buttons, HomePageLocators.answers_text_locator, Questions.expected_question_text))
    def test_to_verification_answers(self, driver, question_buttons, answers_text_locator, expected_question_text):
        home_page = HomePage(driver)
        text = home_page.get_text_answers(question_buttons, answers_text_locator)
        assert text == expected_question_text

    @allure.title('Тест для проверки перехода на главную страницу дзена при клике на логотип "Яндекс"')
    @allure.description('1.Клик по логотипу "Яндекс"'
                      '2.Переход на новую вкладку, загрузка страницы'
                       '3.Сравнить ожидаемый и фактический URL')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.yandex_logo_click()
        main_page.go_to_new_tab()
        time.sleep(5)
        url = main_page.get_current_url()
        assert url == Urls.dzen_url 

    @allure.title('Тест для проверки перехода на главную страницу "Яндекс.самоката" при клике на логотип самоката')
    @allure.description('1.Клик по кнопке заказать'
                        '2.Клик по логотипу "самокат"'
                        '3.Сравнить ожидаемый и фактический URL')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        home_page = HomePage(driver)
        home_page.scroll_and_click_order_button()
        main_page.scooter_logo_click()
        time.sleep(5)
        url = main_page.get_current_url()
        assert url == Urls.scooter_url