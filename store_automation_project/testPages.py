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
                #load a default firefox profile if found
                ff_profile_path = os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
                ff_default_files = os.listdir(ff_profile_path)
                ff_default_profile = os.path.join(ff_profile_path, ff_default_files[0])
                cls.driver = webdriver.Firefox(firefox_profile=ff_default_profile)
            except Exception as inst:
                #no default firefox profile
                cls.driver = webdriver.Firefox()
        else:
            cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

        cls.main_page = MainPage(cls.driver)
        cls.main_page.open('')
        cls.shipping_page = ShippingPage(cls.driver)
        cls.verification_page = VerificationPage(cls.driver)
        cls.billing_page = BillingPage(cls.driver)
        cls.review_page = ReviewPage(cls.driver)


    #Start with Main Page
    def test_page_load(self):
        self.assertTrue(self.main_page.check_page_loaded(),'Failed to load main page')

    def test_add_h_a_kit(self):
        self.assertTrue(self.main_page.add_h_a_kit(1),'Failed to add health and ancestry kit')

    def test_add_a_kit(self):
        self.assertTrue(self.main_page.add_a_kit(1),'Failed to add ancestry kit')

    def test_add_names_to_kits(self):
        self.assertTrue(self.main_page.add_names_to_kits(['Victor Magana','Julius Caesar','Emiliano Zapata','Maximus Meridius','Don Quixote']),'Failed to set name for kits')

    def test_click_continue(self):
        self.shipping_page = self.main_page.click_continue_button()
        time.sleep(5)
        self.assertEqual(self.shipping_page.get_url(), 'https://store.23andme.com/en-us/shipping/','Failed to click continue button')

    #Next Shipping Page
    def test_shipping_page_load(self):
        self.assertTrue(self.shipping_page.check_page_loaded(),'Failed to load Shipping home page')

    def test_shipping_firstname(self):
        self.assertTrue(self.shipping_page.enter_firstname('Victor'),'Failed to set Shipping firstname')

    def test_shipping_lastname(self):
        self.assertTrue(self.shipping_page.enter_lastname('Magana'),'Failed to set Shipping lastname')

    def test_shipping_co_name(self):
        self.assertTrue(self.shipping_page.enter_company('AutomationForce'),'Failed to set Shipping company name')

    def test_shipping_address(self):
        self.assertTrue(self.shipping_page.enter_address('411 S. Main Street'), 'Failed to set Shipping address')

    def test_shipping_apt(self):
        self.assertTrue(self.shipping_page.enter_apt('#1511'),'Failed to set Shipping apartment number')

    def test_shipping_city(self):
        self.assertTrue(self.shipping_page.enter_city('Orange'),'Failed to set Shipping city')

    def test_shipping_state(self):
        self.assertTrue(self.shipping_page.select_state('California'),'Failed to set Shipping state')

    def test_shipping_zip_code(self):
        self.assertTrue(self.shipping_page.enter_zipcode('92868'),'Failed to set Shipping zipcode')

    def test_shipping_country(self):
        self.assertTrue(self.shipping_page.select_country('United States'),'Failed to set Shipping country')

    def test_shipping_method(self):
        self.assertTrue(self.shipping_page.select_shipping_method('Express (2-3 bus. days) - $41.95'),'Failed to set Shipping method')

    def test_shipping_email(self):
        self.assertTrue(self.shipping_page.enter_email('user@automationforce.com'),'Failed to set Shipping email')

    def test_shipping_phone(self):
        self.assertTrue(self.shipping_page.enter_phone('949-714-1234'),'Failed to set Shipping phone')

    def test_shipping_continue(self):
        self.verification_page = self.shipping_page.enter_continue_button()
        time.sleep(10)
        shipping_page_url = self.shipping_page.get_url()
        print shipping_page_url
        self.assertEqual(shipping_page_url,'https://store.23andme.com/en-us/verifyaddress/','Failed to click Shipping continue button')

    #Next verification page
    def test_verification_page_load(self):
        self.assertTrue(self.verification_page.check_page_loaded(),'Failed to load verification page')

    def test_verification_continue(self):
        self.verification_page = self.verification_page.click_verified_button()
        time.sleep(10)
        self.assertEqual(self.verification_page.get_url(),'https://store.23andme.com/en-us/payment/','Failed to click Verification continue button')

    #Next Billing Page
    def test_billing_page_load(self):
        self.assertTrue(self.billing_page.check_page_loaded(), 'Failed to load Billing home page')

    def test_billiing_enter_cc_number(self):
        self.assertTrue(self.billing_page.enter_creditcard_number('4111 1111 1111 1111'),'Failed to enter Billing credit card number')

    def test_billing_enter_exp_date(self):
        self.assertTrue(self.billing_page.enter_expiration_date('09/2020'),'Failed to enter Billing expiration date')

    def test_billing_enter_ccv(self):
        self.assertTrue(self.billing_page.enter_ccv_code('411'),'Failed to enter Billing CCV code')

    def test_billing_address(self):
        self.assertTrue(self.billing_page.click_address(),'Failed to click Billing address')

    def test_billing_continue(self):
        self.verification_page = self.billing_page.click_continue_button()
        time.sleep(5)
        self.assertEqual(self.verification_page.get_url(),'https://store.23andme.com/en-us/review/','Failed to click continue on the billing page')


    #Next Review page
    def test_review_page_load(self):
        self.assertTrue(self.review_page.check_page_loaded(),'Failed to load Verification home page')

    def test_review_accept(self):
        self.assertTrue(self.review_page.click_accept_order(),'Failed to click Verification accept order checkbox')

    def test_review_continue(self):
        self.assertTrue(self.review_page.click_submit_button(),'Failed to click Verification button')

    def test_review_check_error(self):
        elem_output_msg = self.review_page.check_for_error()
        self.assertTrue('We were unable to process your payment as your credit card information was invalid' not in elem_output_msg, elem_output_msg)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_page_load'))
    suite.addTest(TestPages('test_add_h_a_kit'))
    suite.addTest(TestPages('test_add_a_kit'))
    suite.addTest(TestPages('test_add_names_to_kits'))
    suite.addTest(TestPages('test_click_continue'))
    suite.addTest(TestPages('test_shipping_page_load'))
    suite.addTest(TestPages('test_shipping_firstname'))
    suite.addTest(TestPages('test_shipping_lastname'))
    suite.addTest(TestPages('test_shipping_co_name'))
    suite.addTest(TestPages('test_shipping_address'))
    suite.addTest(TestPages('test_shipping_apt'))
    suite.addTest(TestPages('test_shipping_city'))
    suite.addTest(TestPages('test_shipping_state'))
    suite.addTest(TestPages('test_shipping_zip_code'))
    suite.addTest(TestPages('test_shipping_country'))
    suite.addTest(TestPages('test_shipping_method'))
    suite.addTest(TestPages('test_shipping_email'))
    suite.addTest(TestPages('test_shipping_phone'))
    suite.addTest(TestPages('test_shipping_continue'))
    suite.addTest(TestPages('test_verification_page_load'))
    suite.addTest(TestPages('test_verification_continue'))
    suite.addTest(TestPages('test_billing_page_load'))
    suite.addTest(TestPages('test_billiing_enter_cc_number'))
    suite.addTest(TestPages('test_billing_enter_exp_date'))
    suite.addTest(TestPages('test_billing_enter_ccv'))
    suite.addTest(TestPages('test_billing_address'))
    suite.addTest(TestPages('test_billing_continue'))
    suite.addTest(TestPages('test_review_page_load'))
    suite.addTest(TestPages('test_review_accept'))
    suite.addTest(TestPages('test_review_continue'))
    suite.addTest(TestPages('test_review_check_error'))



    #run test in the added rder, otherwise it will be alphabetical order
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main(verbosity=2)
