from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Base class with methods that will be used in every page

class BasePage(object):

    def __init__(self,driver,base_url="http://toolsqa.com/automation-practice-form/"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element_sub(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements_sub(self,*locator):
        return self.driver.find_elements(*locator)

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
