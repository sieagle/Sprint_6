import allure
from dictionary.order_page_dictionary import User
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locator.order_page_locators import OrderPageLocators

class TestOrderPage:
    @allure.title('тест на оформление заказа через кнопку заказа в хедере')
    @allure.description('1.Принять куки'
                        '2.Кликнуть кнопку заказать в хедере'
                        '3.Заполнить форму о себе и нажать далее'
                        '4.Заполнить форму о заказе и нажать заказать в поле заказа'
                        '5.Дождаться формы "заказ принят"')
    def test_order_by_header_order_button_true(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookie()
        order_page = OrderPage(driver)
        home_page.find_order_button().click()
        order_page.all_forms_filled_out(User.user_2)
        assert home_page.wait_for_element(OrderPageLocators.text_order_placed)

    @allure.title('тест на оформление заказа через кнопку заказа на странице')
    @allure.description('1.Скролл до кнопки заказать на странице'
                        '2. Кликнуть кнопку заказа на странице'
                        '3.Заполнить форму о себе и нажать далее'
                        '4.Заполнить форму о заказе и нажать заказать в поле заказа'
                        '5.Дождаться формы "заказ принят"')
    def test_order_by_bottom_order_button_true(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookie()
        home_page.scroll_and_click_order_button()
        order_page = OrderPage(driver)
        order_page.all_forms_filled_out(User.user_1)
        assert home_page.wait_for_element(OrderPageLocators.text_order_placed)