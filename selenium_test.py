from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re, time

class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.demoqa_URL = "http://demoqa.com/";
        self.store_URL = "http://store.demoqa.com/";
        self.form_URL = "http://toolsqa.com/automation-practice-form/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()

    def test_fill_form(self):
        driver = self.driver
        driver.get(self.form_URL)
        elem_fname = driver.find_element_by_name('firstname')
        elem_fname.clear()
        elem_fname.send_keys('Victor')
        elem_lname = driver.find_element_by_name('lastname')
        elem_lname.clear()
        elem_lname.send_keys('Magana')
        driver.find_element_by_id('sex-0').click()
        driver.find_element_by_id('exp-0').click()
        elem_date = driver.find_element_by_id('datepicker')
        elem_date.clear()
        elem_date.send_keys('01/01/17')
        driver.find_element_by_id('profession-1').click()
        driver.find_element_by_id('tool-1').click()
        driver.find_element_by_id('tool-2').click()
        Select(driver.find_element_by_id('continents')).select_by_visible_text('North America')
        oListSelect = Select(driver.find_element_by_id('selenium_commands'))
        elem_list = oListSelect.options
        for item in elem_list:
            item.click()
            print item.text

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.demoqa_URL)
        driver.find_element_by_link_text('Registration').click()
        self.assertEqual(driver.title,'Demoqa | Just another WordPress site','Page title is not correct')

        elem_fname = driver.find_element_by_id('name_3_firstname')
        elem_fname.clear()
        elem_fname.send_keys('Victor')
        elem_lname = driver.find_element_by_id('name_3_lastname')
        elem_lname.clear()
        elem_lname.send_keys('Magana')
        #marital status
        driver.find_element_by_xpath("(//input[@name='radio_4[]'])[2]").click()
        #hobby
        driver.find_element_by_xpath("(//input[@name='checkbox_5[]'])[2]").click()
        #country
        Select(driver.find_element_by_id('dropdown_7')).select_by_visible_text('United States')
        #birthdate
        Select(driver.find_element_by_id('mm_date_8')).select_by_visible_text('3')
        Select(driver.find_element_by_id('dd_date_8')).select_by_visible_text('10')
        Select(driver.find_element_by_id('yy_date_8')).select_by_visible_text('2000')
        #phone
        elem_phone = driver.find_element_by_id('phone_9')
        elem_phone.clear()
        elem_phone.send_keys('7141234567')
        #username
        elem_username = driver.find_element_by_id('username')
        elem_username.clear()
        elem_username.send_keys('vmagana_new')
        #email
        elem_email = driver.find_element_by_id('email_1')
        elem_email.clear()
        elem_email.send_keys('vmagananew@email.com')
        #about yourself textbox
        elem_about_textbox = driver.find_element_by_id('description')
        elem_about_textbox.clear()
        elem_about_textbox.send_keys('Sample test setup info')
        #password
        elem_password = driver.find_element_by_id('password_2')
        elem_password.clear()
        elem_password.send_keys('$TR(!!!)ngWORD')
        #confirm password
        elem_confirm_password = driver.find_element_by_id('confirm_password_password_2')
        elem_confirm_password.clear()
        elem_confirm_password.send_keys('$TR(!!!)ngWORD') #$TR(!!!)ngWORD
        #password strength indicator
        password_strength = driver.find_element_by_id('piereg_passwordStrength').text
        self.assertEqual(password_strength,'Strong','Password is not Strong')

        #submit
        driver.find_element_by_name('pie_submit').click()
        time.sleep(10)
        bool_login_error = self.is_element_present(By.CLASS_NAME,'piereg_login_error')
        #if login failed
        if bool_login_error is True:
            self.assertFalse(bool_login_error, driver.find_element_by_class_name('piereg_login_error').text)
        else:
        #if login was good
            good_msg = driver.find_element_by_class_name('piereg_message').text
            print good_msg


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == '__main__':
    unittest.main(verbosity=2)



