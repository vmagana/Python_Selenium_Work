from selenium.webdriver.common.by import By

# for maintainability we separate web objects by page name

class MainPageLocators(object):
  LOGO = (By.CLASS_NAME, 'main-logo')
  ADD_HEALTH_ANCESTRY_KIT = (By.CSS_SELECTOR, 'span.quantity-control-button.js-add-kit')
  COUNTER_HEALTH_ANCESTRY_KIT = (By.CSS_SELECTOR, 'span#text-health-kit-count.quantity-control-count')
  ADD_ANCESTRY_KIT = (By.CSS_SELECTOR, 'span.quantity-control-button.js-add-ancestry-kit')
  COUNTER_ANCESTRY_KIT = (By.CSS_SELECTOR, 'span#text-ancestry-kit-count.quantity-control-count')
  KIT_LIST = (By.CLASS_NAME, 'kit-list')
  KIT_LIST_NAMES = (By.NAME, 'name')
  CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.submit.button-continue')
  SHIPPING_PAGE_URL = 'https://store.23andme.com/en-us/shipping/'


class ShippingPageLocators(object):
  SHIPPING_LOGO = (By.CLASS_NAME, 'progress-banner-heading')
  SHIPPING_FIRSTNAME = (By.ID, 'id_first_name')
  SHIPPING_LASTNAME = (By.ID, 'id_last_name')
  SHIPPING_COMPANY = (By.ID, 'id_company')
  SHIPPING_ADDRESS = (By.ID, 'id_address')
  SHIPPING_APT_BUILDING = (By.ID, 'id_address2')
  SHIPPING_CITY = (By.ID, 'id_city')
  SHIPPING_STATE = (By.NAME, 'state')#select
  SHIPPING_ZIPCODE = (By.ID, 'id_postal_code')
  SHIPPING_COUNTRY = (By.ID, 'id_country')#select
  SHIPPING_METHOD = (By.ID, 'id_shipping_method')#select
  SHIPPING_EMAIL = (By.ID, 'id_email')
  SHIPPING_PHONE = (By.ID, 'id_int_phone')
  SHIPPING_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.submit.button-continue')
  VERIFICATION_PAGE_URL = 'https://store.23andme.com/en-us/verifyaddress/'

class VerificationPageLocators(object):
  VERIFICATION_LOGO = (By.CLASS_NAME, 'verification-summary')
  VERIFICATION_SUGGESTION = (By.CLASS_NAME, 'verify suggestion')
  VERIFICATION_SHIP_UNVERIFIED = (By.CLASS_NAME, 'button-continue use-unverified')
  VERIFICATION_SHIP_VERIFIED = (By.CLASS_NAME, 'button-continue')
  BILLING_PAGE_URL = 'https://store.23andme.com/en-us/payment/'


class BillingPageLocators(object):
  BILLING_LOGO = (By.CLASS_NAME, 'progress-banner-heading')
  BILLING_CREDIT_CARD = (By.ID, 'credit-card-number')
  BILLING_EXPIRATION_DATE = (By.ID, 'expiration')
  BILLLING_CVV_NUMBER = (By.ID, 'cvv')
  BILLING_ADDRESS_SAME = (By.ID, 'id_address_select_0')
  BILLING_CONTINUE_BUTTON = (By.NAME, 'submitPayment')
  REVIEW_PAGE_URL = 'https://store.23andme.com/en-us/review/'


class ReviewPageLocators(object):
  REVIEW_LOGO = (By.CLASS_NAME, 'progress-banner-heading')
  REVIEW_ACCEPT_ORDER = (By.CLASS_NAME, 'tos-checkbox')
  REVIEW_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input.submit.button-continue')
  REVIEW_SUBMIT_ERROR = (By.CSS_SELECTOR, 'span.payment.error')
  #Error Message:
  #We were unable to process your payment as your credit card information was invalid.
  #Please re-enter your credit card information or add new credit card details.


