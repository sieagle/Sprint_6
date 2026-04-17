from locator.order_page_locators import OrderPageLocators
import allure
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнение поля имя')
    def send_name_to_name_field(self, text):
        self.send_keys(OrderPageLocators.name_field, text)
    
    @allure.step('Заполнение поля фамилия')
    def send_last_name_to_name_field(self, text):
        self.send_keys(OrderPageLocators.last_name_field, text)
    
    @allure.step('Заполнение поля адресс')
    def send_address_to_address_field(self, text):
        self.send_keys(OrderPageLocators.address_field, text)
    
    @allure.step('Выбор станции метро')
    def send_metro_station_to_metro_station_field(self):
        self.click_button(OrderPageLocators.metro_station_field)
        self.scroll_to_locator(OrderPageLocators.name_metro_station)
        self.click_button(OrderPageLocators.name_metro_station)

    @allure.step('Заполнение поля номер телефона')
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys(OrderPageLocators.telephone_field, text)

    @allure.step('Клик на кнопку дальше')
    def click_on_the_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Полное заполнение информации о пользователе')
    def complete_send_field_about_person(self, user):
        self.send_name_to_name_field(user[1])
        self.send_last_name_to_name_field(user[2])
        self.send_address_to_address_field(user[3])
        self.send_metro_station_to_metro_station_field()
        self.send_telephone_number_to_telephone_number_field(user[4])
        self.click_on_the_next_button()

    #Страница информация о заказе
    
    @allure.step('Выбор времени доставки')
    def send_time_to_deliver_field(self):
        self.click_button(OrderPageLocators.time_to_deliver_field)
        self.click_button(OrderPageLocators.day_and_mounth)

    @allure.step('Выбор периода аренды')
    def send_period_time(self):
        self.click_button(OrderPageLocators.rent_period_time)
        self.click_button(OrderPageLocators.five_days_period_time)

    @allure.step('Выбор цвета')    
    def choose_color(self):
        self.click_button(OrderPageLocators.checkbox_grey)

    @allure.step('Комментарий курьеру')
    def send_comment_to_comment_field(self, text):
        self.send_keys(OrderPageLocators.info_for_courier, text)

    @allure.step('Клик на кнопку заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('Полное заполнение информации о заказе')
    def complete_send_field_about_order(self, text):
        self.send_time_to_deliver_field()
        self.send_period_time()
        self.choose_color()
        self.send_comment_to_comment_field(text)
        self.click_order_button()

    #Подтверждение заказа
    
    @allure.step('Клик по кнопке нет')
    def click_button_no(self):
        self.click_button(OrderPageLocators.not_button)

    @allure.step('Клик по кнопке да')
    def click_button_yes(self):
        self.click_button(OrderPageLocators.yes_button)

    @allure.step('Полный цикл заказа самоката')
    def all_forms_filled_out(self, user):
        self.complete_send_field_about_person(user)
        self.complete_send_field_about_order(user[6])
        self.click_button_yes()
    
    #Стрвница подтвержденного заказа
    
    @allure.step('Найти инфо о заказе')
    def check_text_title(self):
        return self.find_and_wait_locator(OrderPageLocators.text_order_placed).is_displayed
    
    @allure.step('Найти кнопку проверки статуса заказа')
    def check_status_button(self): 
        return self.find_and_wait_locator(OrderPageLocators.status_button).is_displayed
