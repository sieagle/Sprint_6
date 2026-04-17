import pytest
from selenium import webdriver
from dictionary.base_page_dictionary import Urls
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.scooter_url)
    yield driver
    driver.quit()
    return driver
