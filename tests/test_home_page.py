import allure
import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.dzen_page import DzenPage
from locator.home_page_locators import HomePageLocators
from dictionary.base_page_dictionary import Urls
from dictionary.home_page_dictionary import Questions

class TestHomePage:
    @allure.title('Тест на проверку того, что на странице 2 кнопки заказать')
    @allure.description('1.Найти кнопку "Заказать" в хедере,' 
                        '2. Проскроллить страницу и найти кнопку "Заказать" в середине страницы')
    def test_two_buttons_in_page(self, driver):
        base_page = BasePage(driver)
        page = HomePage(driver)
        orderTopButton = page.find_order_button()
        base_page.element_is_visible(orderTopButton)
        assert orderTopButton.is_displayed(), f"{orderTopButton} не отображается на странице"
        orderBottomButton = page.scroll_to_bottom_order_button()
        base_page.element_is_visible(orderBottomButton)
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
                        '3.Дождаться элемента кнопка "главная"'
                        '4.Сравнить ожидаемый и фактический URL')
    def test_logo_yandex(self, driver):
        base_page = BasePage(driver)
        base_page.yandex_logo_click()
        base_page.go_to_new_tab()
        dzen_page = DzenPage(driver)
        dzen_page.check_elements()
        url = base_page.get_current_url()
        assert url == Urls.dzen_url

    @allure.title('Тест для проверки перехода на главную страницу "Яндекс.самоката" при клике на логотип самоката')
    @allure.description('1.Принять куки'
                        '2.Клик по кнопке заказать'
                        '3.Клик по логотипу "самокат"'
                        '4.Дождаться элемента кнопка "заказать"'
                        '5.Сравнить ожидаемый и фактический URL')
    def test_logo_scooter(self, driver):
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        home_page.accept_cookie
        home_page.scroll_and_click_order_button()
        base_page.scooter_logo_click()
        base_page.find_and_wait_locator(HomePageLocators.header_order_button)
        url = base_page.get_current_url()
        assert url == Urls.scooter_url