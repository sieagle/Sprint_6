from selenium.webdriver.common.by import By

class OrderPageLocators:
    
    #Страница информация о себе
    name_field = (By.XPATH, ".//input[@placeholder = '* Имя']")
    last_name_field = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    address_field = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    #search_metro_station = (By.XPATH, ".//div[@class = 'select-search__select']")
    name_metro_station = (By.XPATH, ".//button [@value = '55']")
    telephone_field = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text() = 'Далее']")
    
    #Страница информация о заказе
    time_to_deliver_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    day_and_mounth = (By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--027']")
    rent_period_time = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    five_days_period_time = (By.XPATH, ".//div[text() = 'пятеро суток']")
    checkbox_black = (By.XPATH, ".//input [@id = 'black']")
    checkbox_grey = (By.XPATH, ".//input [@id = 'grey']")
    info_for_courier = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    back_button = (By.XPATH, ".//button[text() = 'Назад']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")
    
    #Подтверждение заказа
    not_button = (By.XPATH, ".//button[text() = 'Нет']")
    yes_button = (By.XPATH, ".//button[text() = 'Да']")
    
    #Заказ оформлен
    text_order_placed = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")