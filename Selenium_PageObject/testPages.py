from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
from pageLocators import *
from testCasesText import test_cases
from pageObjects import *


class TestPages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference('browser.download.folderList',2)
        ff_profile.set_preference("browser.download.manager.showWhenStarting", False)
        ff_profile.set_preference("browser.download.dir", os.getcwd())
        ff_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        cls.driver = webdriver.Firefox(firefox_profile=ff_profile)

        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.base_url = ("http://toolsqa.com/automation-practice-form/")
        cls.driver.get(cls.base_url)
        cls.main_page = MainPage(cls.driver)

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        #page = MainPage(self.driver)
        self.assertTrue(self.main_page.check_page_loaded())

    def test_set_firstname(self):
        print "\n" + str(test_cases(1))
        self.assertTrue(self.main_page.set_firstname('Victor'),'Failed to set firstname')

    def test_set_lastname(self):
        print "\n" + str(test_cases(2))
        self.assertTrue(self.main_page.set_lastname('Magana'),'Failed to set lastname')

    def test_select_male_female(self):
        print "\n" + str(test_cases(3))
        self.assertTrue(self.main_page.select_male_female('Male'),'Failed to select Male or Female option')

    def test_select_experience(self):
        print "\n" + str(test_cases(4))
        self.assertTrue(self.main_page.select_years_experience('5'),'Failed to select years of experience')

    def test_select_date(self):
        print "\n" + str(test_cases(5))
        self.assertTrue(self.main_page.select_date('01/01/2017'),'Failed to set the date')

    def test_select_profession(self):
        print "\n" + str(test_cases(6))
        self.assertTrue(self.main_page.select_profession('Automation Tester'),'Failed to set profession option')

    def test_select_automation_tool(self):
        print "\n" + str(test_cases(7))
        self.assertTrue(self.main_page.select_automation_tools('Selenium IDE'),'Failed to set automation tool')

    def test_select_continents(self):
        print "\n" + str(test_cases(8))
        self.assertTrue(self.main_page.select_continents('North America'),'Failed to set continent option')

    def test_select_selenium_cmds(self):
        print "\n" + str(test_cases(9))
        self.assertTrue(self.main_page.set_selenium_cmds('Browser Commands'),'Failed to set selenium commands')

    def test_download_file(self):
        print "\n" + str(test_cases(10))
        self.assertTrue(self.main_page.download_file('Test-File-to-Download.xlsx'),'Failed to download file')

    def test_upload_file(self):
        print "\n" + str(test_cases(11))
        self.assertTrue(self.main_page.upload_file('bear.jpg'),'Failed to upload file')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_page_load'))
    suite.addTest(TestPages('test_set_firstname'))
    suite.addTest(TestPages('test_set_lastname'))
    suite.addTest(TestPages('test_select_male_female'))
    suite.addTest(TestPages('test_select_experience'))
    suite.addTest(TestPages('test_select_date'))
    suite.addTest(TestPages('test_select_profession'))
    suite.addTest(TestPages('test_select_automation_tool'))
    suite.addTest(TestPages('test_select_continents'))
    suite.addTest(TestPages('test_select_selenium_cmds'))
    suite.addTest(TestPages('test_download_file'))
    suite.addTest(TestPages('test_upload_file'))
    #run test in the added rder, otherwise it will be alphabetical order
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main(verbosity=2)
