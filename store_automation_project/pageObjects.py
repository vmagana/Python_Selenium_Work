import os, time, re
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from basePage import BasePage
from pageLocators import MainPageLocators
from pageLocators import ShippingPageLocators
from pageLocators import VerificationPageLocators
from pageLocators import BillingPageLocators
from pageLocators import ReviewPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    home_url = 'https://store.23andme.com/en-us'

    def __init__(self, driver):
        super(MainPage,self).__init__(driver,self.home_url)
        self.MainPage_Locators = MainPageLocators()

    def check_page_loaded(self):
        #return True if self.find_element_sub(*self.MainPage_Locators.LOGO) else False
        elem_href = self.find_element_sub(*self.MainPage_Locators.LOGO).get_attribute('href')
        if elem_href == 'https://www.23andme.com/en-us':
            return True
        else:
            return False

    def add_h_a_kit(self, count):
        for num in range(count):
            self.find_element_sub(*self.MainPage_Locators.ADD_HEALTH_ANCESTRY_KIT).click()
            #need to slow down otherwise click does not get recorded
            time.sleep(5)
        #verify the counter has the correct amount
        elem_count = self.find_element_sub(*self.MainPage_Locators.COUNTER_HEALTH_ANCESTRY_KIT)
        if int(elem_count.text) == count:
            return True
        else:
            return False

    def add_a_kit(self, count):
        for num in range(count):
            self.find_element_sub(*self.MainPage_Locators.ADD_ANCESTRY_KIT).click()
            # need to slow down otherwise click does not get recorded
            time.sleep(5)
        # verify the counter has the correct amount
        elem_count = self.find_element_sub(*self.MainPage_Locators.COUNTER_ANCESTRY_KIT)
        if int(elem_count.text) == count:
            return True
        else:
            return False

    def add_names_to_kits(self,names_list):
        elem_kit = self.find_element_sub(*self.MainPage_Locators.KIT_LIST)
        elem_list = elem_kit.find_elements(*self.MainPage_Locators.KIT_LIST_NAMES)
        for item,name in zip(elem_list,names_list):
            item.send_keys(name)
            time.sleep(1)
        elem_set_names = elem_kit.find_elements(*self.MainPage_Locators.KIT_LIST_NAMES)
        for item,name in zip(elem_set_names,names_list):
            if item.get_attribute('value') != name:
                return False

        return True

    def click_continue_button(self):
        elem_button = self.find_element_sub(*self.MainPage_Locators.CONTINUE_BUTTON)
        #wait until button is enabled,then click
        timeout_counter = 0
        while elem_button.get_attribute('class') == 'submit button-continue button-disabled':
            time.sleep(2)
            timeout_counter += 1
            if timeout_counter > 5:
                return False
        elem_button.click()
        #self.click_element_sub(*self.MainPage_Locators.CONTINUE_BUTTON)
        return ShippingPage(self.driver)



class ShippingPage(BasePage):
    home_url = 'https://store.23andme.com/en-us/shipping/'

    def __init__(self, driver):
        super(ShippingPage, self).__init__(driver,self.home_url)
        self.ShippingPage_Locators = ShippingPageLocators()

    def check_page_loaded(self):
        elem_shipping = self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_LOGO).text
        if elem_shipping == 'SHIPPING' and self.get_url() == self.home_url:
            return True
        else:
            return False

    def enter_firstname(self,firstname):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_FIRSTNAME).send_keys(firstname)
        return True

    def enter_lastname(self,lastname):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_LASTNAME).send_keys(lastname)
        return True

    def enter_company(self,company):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_COMPANY).send_keys(company)
        return True

    def enter_address(self,address):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_ADDRESS).send_keys(address)
        return True

    def enter_apt(self,apt):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_APT_BUILDING).send_keys(apt)
        return True

    def enter_city(self,city):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_CITY).send_keys(city)
        return True

    def select_state(self,state):
        Select(self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_STATE)).select_by_visible_text(state)
        return True

    def enter_zipcode(self,zipcode):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_ZIPCODE).send_keys(zipcode)
        return True

    def select_country(self,country):
        Select(self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_COUNTRY)).select_by_visible_text(country)
        return True

    def select_shipping_method(self,method):
        elem_ship_methods = Select(self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_METHOD)).options
        for item in elem_ship_methods:
            if item.text == method:
                item.click()
                return True
        return False

    def enter_email(self,email):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_EMAIL).send_keys(email)
        return True

    def enter_phone(self,phone):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_PHONE).send_keys(phone)
        return True

    def enter_continue_button(self):
        self.find_element_sub(*self.ShippingPage_Locators.SHIPPING_CONTINUE_BUTTON).click()
        return VerificationPage(self.driver)


class VerificationPage(BasePage):
    home_url = 'https://store.23andme.com/en-us/verifyaddress/'

    def __init__(self, driver):
        super(VerificationPage, self).__init__(driver, self.home_url)
        self.VerificationPage_Locators = VerificationPageLocators()

    def check_page_loaded(self):
        elem_verify_text = self.find_element_sub(*self.VerificationPage_Locators.VERIFICATION_LOGO).text
        elem_search_text = re.search('Address Verification', elem_verify_text)
        if elem_verify_text and self.get_url() == self.home_url:
            return True
        else:
            return False

    def click_verified_button(self):
        self.find_element_sub(*self.VerificationPage_Locators.VERIFICATION_SHIP_VERIFIED).click()
        return BillingPage(self.driver)


class BillingPage(BasePage):
    home_url ='https://store.23andme.com/en-us/payment/'

    def __init__(self,driver):
        super(BillingPage,self).__init__(driver, self.home_url)
        self.BillingPage_Locators = BillingPageLocators()

    def check_page_loaded(self):
        elem_billing = self.find_element_sub(*self.BillingPage_Locators.BILLING_LOGO).text
        if elem_billing == 'BILLING' and self.get_url() == self.home_url:
            return True
        else:
            return False

    def enter_creditcard_number(self,ccnumber):
        #switch to credit card number iframe
        elem_frame = self.driver.switch_to.frame(self.driver.find_element_by_id('braintree-hosted-field-number'))
        self.find_element_sub(*self.BillingPage_Locators.BILLING_CREDIT_CARD).send_keys(ccnumber)
        #switch back out of iframe
        self.driver.switch_to_default_content()
        return True

    def enter_expiration_date(self,expdate):
        # switch to credit card number iframe
        elem_frame = self.driver.switch_to.frame(self.driver.find_element_by_id('braintree-hosted-field-expirationDate'))
        self.find_element_sub(*self.BillingPage_Locators.BILLING_EXPIRATION_DATE).send_keys(expdate)
        #switch back out of iframe
        self.driver.switch_to_default_content()
        return True

    def enter_ccv_code(self,ccv_code):
        # switch to credit card number iframe
        elem_frame = self.driver.switch_to.frame(
        self.driver.find_element_by_id('braintree-hosted-field-cvv'))
        self.find_element_sub(*self.BillingPage_Locators.BILLLING_CVV_NUMBER).send_keys(ccv_code)
        #switch back out of iframe
        self.driver.switch_to_default_content()
        return True

    def click_address(self):
        self.find_element_sub(*self.BillingPage_Locators.BILLING_ADDRESS_SAME).click()
        return True

    def click_continue_button(self):
        self.find_element_sub(*self.BillingPage_Locators.BILLING_CONTINUE_BUTTON).click()
        return VerificationPage(self.driver)


class ReviewPage(BasePage):
    home_url = 'https://store.23andme.com/en-us/review/'

    def __init__(self,driver):
        super(ReviewPage,self).__init__(driver,self.home_url)
        self.ReviewPage_Locators = ReviewPageLocators()

    def check_page_loaded(self):
        elem_review = self.find_element_sub(*self.ReviewPage_Locators.REVIEW_LOGO).text
        if elem_review == 'REVIEW' and self.get_url() == self.home_url:
            return True
        else:
            return False

    def click_accept_order(self):
        self.find_element_sub(*self.ReviewPage_Locators.REVIEW_ACCEPT_ORDER).click()
        return True

    def click_submit_button(self):
        self.find_element_sub(*self.ReviewPage_Locators.REVIEW_SUBMIT_BUTTON).click()
        return True

    def check_for_error(self):
        elem_error_msg = self.find_element_sub(*self.ReviewPage_Locators.REVIEW_SUBMIT_ERROR).text
        return elem_error_msg







