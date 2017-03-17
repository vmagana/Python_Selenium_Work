from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Base class with methods that will be used in every page

class BasePage(object):

    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, 15)

    def find_element_sub(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements_sub(self,*locator):
        return self.driver.find_elements(*locator)

    def click_element_sub(self,*locator):
        element_button = self.wait.until(EC.presence_of_element_located(*locator))
        element_button.click()

    def open(self,url):
        url=self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover_sub(self,*locator):
        element = self.find_element_sub(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
