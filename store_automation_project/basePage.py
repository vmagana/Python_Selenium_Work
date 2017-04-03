from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Base class with methods that will be used in every page

class BasePage(object):
    def __init__(self, driver, home_url):
        self.driver = driver
        self.home_url = home_url
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element_sub(self, *locator):
        # use WebDriverWait to wait for element
        return self.wait.until(lambda driver: self.driver.find_element(*locator), 'Timeout finding element')

    def find_elements_sub(self, *locator):
        # use WebDriverWait to wait for element
        return self.wait.until(lambda driver: self.driver.find_elements(*locator), 'Timeout finding elements')

    def click_element_sub(self, *locator):
        # use WebDriverWait to wait for element
        element_button = self.wait.until(lambda driver: driver.find_elements(*locator), 'Timeout clicking on element')
        element_button.click()

    def open(self, url):
        url = self.home_url + url
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def mouse_hover_sub(self, *locator):
        # use WebDriverWait to wait for element
        element = self.wait.until(lambda driver: self.driver.find_element(*locator), 'Timeout finding element for mouse hover')
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
