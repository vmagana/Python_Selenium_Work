#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
from pageLocators import *
from pageObjects import *


class TestPages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        try_use_default_profile = 0
        if try_use_default_profile:
            try:
                # load a default firefox profile if found
                ff_profile_path = os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
                ff_default_files = os.listdir(ff_profile_path)
                ff_default_profile = os.path.join(ff_profile_path, ff_default_files[0])
                cls.driver = webdriver.Firefox(firefox_profile=ff_default_profile)
            except Exception as inst:
                # no default firefox profile
                cls.driver = webdriver.Firefox()
        else:
            cls.driver = webdriver.Firefox()

        #cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        # Pages so they can be shared across test methods
        cls.main_page = MainPage(cls.driver, 'https://store.23andme.com/en-us')
        cls.main_page.open('')
        cls.shipping_page = None
        cls.verification_page = None
        cls.billing_page = None
        cls.review_page = None

    # Start with Main Page
    def test_main_page(self):
        self.assertTrue(self.main_page.check_page_loaded(), 'Failed to load main page')
        self.assertTrue(self.main_page.add_h_a_kit(1), 'Failed to add health and ancestry kit')
        self.assertTrue(self.main_page.add_a_kit(1), 'Failed to add ancestry kit')
        self.assertTrue(self.main_page.add_names_to_kits(
            ['Victor Magana', 'Julius Caesar', 'Emiliano Zapata', 'Maximus Meridius', 'Don Quixote']),
                        'Failed to set name for kits')
        TestPages.shipping_page = self.main_page.click_continue_button()
        time.sleep(2)
        self.assertEqual(self.shipping_page.get_page_url(), self.shipping_page.home_url, 'Failed to click continue button')

    # Next Shipping Page
    def test_shipping_page(self):
        self.assertTrue(self.shipping_page.check_page_loaded(), 'Failed to load Shipping home page')
        self.assertTrue(self.shipping_page.enter_firstname('Victor'), 'Failed to set Shipping firstname')
        self.assertTrue(self.shipping_page.enter_lastname('Magana'), 'Failed to set Shipping lastname')
        self.assertTrue(self.shipping_page.enter_company('AutomationForce'), 'Failed to set Shipping company name')
        self.assertTrue(self.shipping_page.enter_address('411 S. Main Street'), 'Failed to set Shipping address')
        self.assertTrue(self.shipping_page.enter_apt('#1511'), 'Failed to set Shipping apartment number')
        self.assertTrue(self.shipping_page.enter_city('Orange'), 'Failed to set Shipping city')
        self.assertTrue(self.shipping_page.select_state('California'), 'Failed to set Shipping state')
        self.assertTrue(self.shipping_page.enter_zipcode('92868'), 'Failed to set Shipping zipcode')
        self.assertTrue(self.shipping_page.select_country('United States'), 'Failed to set Shipping country')
        self.assertTrue(self.shipping_page.select_shipping_method('Express'), 'Failed to set Shipping method')
        self.assertTrue(self.shipping_page.enter_email('user@automationforce.com'), 'Failed to set Shipping email')
        self.assertTrue(self.shipping_page.enter_phone('949-714-1234'), 'Failed to set Shipping phone')
        TestPages.verification_page = self.shipping_page.enter_continue_button()
        time.sleep(10)
        self.assertEqual(self.verification_page.get_page_url(), self.verification_page.home_url)

    # Next verification page
    def test_verification_page(self):
        self.assertTrue(self.verification_page.check_page_loaded(), 'Failed to load verification page')
        TestPages.billing_page = self.verification_page.click_verified_button()
        time.sleep(10)
        self.assertEqual(self.billing_page.get_page_url(), self.billing_page.home_url)

    # Next Billing Page
    def test_billing_page(self):
        self.assertTrue(self.billing_page.check_page_loaded(), 'Failed to load Billing home page')
        self.assertTrue(self.billing_page.enter_creditcard_number('4111 1111 1111 1111'),
                        'Failed to enter Billing credit card number')
        self.assertTrue(self.billing_page.enter_expiration_date('09/2020'), 'Failed to enter Billing expiration date')
        self.assertTrue(self.billing_page.enter_ccv_code('411'), 'Failed to enter Billing CCV code')
        self.assertTrue(self.billing_page.click_address(), 'Failed to click Billing address')
        TestPages.review_page = self.billing_page.click_continue_button()
        time.sleep(5)
        self.assertEqual(self.review_page.get_page_url(), self.review_page.home_url)

    # Next Review page
    def test_review_page(self):
        self.assertTrue(self.review_page.check_page_loaded(), 'Failed to load Verification home page')
        self.assertTrue(self.review_page.click_accept_order(), 'Failed to click Verification accept order checkbox')
        self.assertTrue(self.review_page.click_submit_button(), 'Failed to click Verification button')
        elem_output_msg = self.review_page.check_for_error()
        self.assertTrue(
            'We were unable to process your payment as your credit card information was invalid' not in elem_output_msg,
            elem_output_msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_main_page'))
    suite.addTest(TestPages('test_shipping_page'))
    suite.addTest(TestPages('test_verification_page'))
    suite.addTest(TestPages('test_billing_page'))
    suite.addTest(TestPages('test_review_page'))

    # run test in the added order, otherwise it will be alphabetical order
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
