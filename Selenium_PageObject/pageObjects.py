from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from basePage import BasePage
import users, time, os
from pageLocators import *
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pywinauto

class MainPage(BasePage):
    def check_page_loaded(self):
        return True if self.find_element_sub(*MainPageLocators.LOGO) else False

    def search_item(self, item):
        self.find_element_sub(*MainPageLocators.SEARCH).send_keys(item)
        self.find_element_sub(*MainPageLocators.SEARCH).send_keys(Keys.ENTER)
        return self.find_element_sub(*MainPageLocators.SEARCH_LIST).text

    def set_firstname(self,firstname):
        self.find_element_sub(*MainPageLocators.FIRSTNAME).send_keys(firstname)
        return True

    def set_lastname(self,lastname):
        self.find_element_sub(*MainPageLocators.LASTTNAME).send_keys(lastname)
        return True

    def select_male_female(self,gender):
        elem_list_results = self.find_elements_sub(*MainPageLocators.MALE_FEMALE)
        for item in elem_list_results:
            if item.get_attribute('value') == gender:
                item.click()
                return True
        return False

    def select_years_experience(self,years):
        elem_list_years = self.find_elements_sub(*MainPageLocators.YEARS_EXPERIENCE)
        for year in elem_list_years:
            if year.get_attribute('value') == years:
                year.click()
                return True
        return False

    def select_date(self,date_data):
        elem_date = self.find_element_sub(*MainPageLocators.DATE)
        elem_date.clear()
        elem_date.send_keys(date_data)
        get_date = elem_date.get_attribute('value')
        if get_date == date_data:
            return True
        return False

    def select_profession(self,profession):
        elem_professions = self.find_elements_sub(*MainPageLocators.PROFESSION)
        for job in elem_professions:
            if job.get_attribute('value') == profession:
                job.click()
                return True
        return False

    def select_automation_tools(self,tool):
        elem_tools = self.find_elements_sub(*MainPageLocators.TOOL)
        for entry in elem_tools:
            if entry.get_attribute('value') == tool:
                entry.click()
                return True
        return False

    def select_continents(self,continent):
        Select(self.find_element_sub(*MainPageLocators.CONTINENTS)).select_by_visible_text(continent)
        elem_option = Select(self.find_element_sub(*MainPageLocators.CONTINENTS)).first_selected_option
        if elem_option.text == continent:
            return True
        return False

    def set_selenium_cmds(self,commands):
        elem_options = Select(self.find_element_sub(*MainPageLocators.SELENIUM_CMDS)).options
        for item in elem_options:
            if item.get_attribute('value') == commands:
                item.click()
                return True
        return False

    def download_file(self,filename):
        self.find_element_sub(*MainPageLocators.DOWNLOAD_FILE).click()
        time.sleep(2)
        fpath = os.getcwd() + '\\' + filename
        if os.path.isfile(fpath):
            return True
        else:
            return False

    def upload_file(self,filename):
        fpath = os.getcwd() + '\\' + filename
        elem_upload_file = self.find_element_sub(*MainPageLocators.UPLOAD_FILE)
        elem_upload_file.clear()
        elem_upload_file.send_keys(fpath)
        elem_name = elem_upload_file.get_attribute('value')
        if elem_name == filename:
            return True
        else:
            return False

    def uploadTest(self,Name_of_File):
        app = pywinauto.application.Application().start()
        mainWindow = app['Upload']  # main windows' title
        #ctrl = mainWindow['Edit']
        mainWindow.SetFocus()
        mainWindow.TypeKeys('TestFile')
        ctrlBis = mainWindow['TestFileSection']  # open file button
        ctrlBis.ClickInput()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


class LoginPage(BasePage):
    def enter_email(self,user):
        self.find_element_sub(*LoginPageLocators.EMAIL).send_keys(users.get_user(user)['email'])

    def enter_password(self,user):
        self.find_element_sub(*LoginPageLocators.PASSWORD).send_keys(users.get_user(user)['password'])

    def click_login_button(self):
        self.find_element_sub(*LoginPageLocators.SUBMIT).click()

    def login(self,user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self,user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_invalid_user(self,user):
        self.login(user)
        return self.find_element_sub(*LoginPageLocators.ERROR_MESSAGE).text


class HomePage(BasePage):
    pass

class SignUpPage(BasePage):
    pass






