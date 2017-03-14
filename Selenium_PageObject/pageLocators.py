from selenium.webdriver.common.by import By

# for maintainability we separate web objects by page name

class MainPageLocators(object):
  LOGO = (By.CLASS_NAME, 'page-title')
  FIRSTNAME = (By.NAME, 'firstname')
  LASTTNAME = (By.NAME, 'lastname')
  MALE_FEMALE = (By.NAME, 'sex')
  YEARS_EXPERIENCE = (By.NAME, 'exp')
  DATE = (By.ID, 'datepicker')
  PROFESSION = (By.NAME, 'profession')
  TOOL = (By.NAME, 'tool')
  CONTINENTS = (By.ID, 'continents')
  SELENIUM_CMDS = (By.ID, 'selenium_commands')
  DOWNLOAD_FILE = (By.LINK_TEXT, 'Test File to Download')
  UPLOAD_FILE = (By.ID, 'photo')


class LoginPageLocators(object):
  EMAIL = (By.ID, 'ap_email')
  PASSWORD = (By.ID, 'ap_password')
  SUBMIT = (By.ID, 'signInSubmit')
  ERROR_MESSAGE = (By.CLASS_NAME, 'a-list-item')