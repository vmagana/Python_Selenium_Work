# Selenium Store Checkout Automation using Python scripts

Selenium using Python scripts showing basic interaction during a store checkout web form

## Getting Started

This project is done so it can be maintained pretty easy by modify page elements if needed without rewriting much code.<br>
There could be timing issues that need to be fined tuned due to delays in response from web pages.

The Selenium page object script fills out a web forms by finding different web page elements<br>

Project breakdown:<br>  
basePage.py - options shared by all web pages<br>
pageLocators.py - contains the elements locators per web page<br>
pageObjects.py - has a method to access each element in the web page<br>  
testPages.py - runs the unit test, each test interacts with one web page element using the same web browser instance<br>
Can be ran in specified order or default alphabetical order<br>

These test were verified on a Windows 7 with Firefox browser.<br>

### Prerequisites

Python 2.7, Selenium Webdriver, gecko firefox driver, python selenium webdriver

## Running the tests

Execute testPages.py

### Break down into the tests
---Home Page---<br>
Starts by opening up a firefox browser instance and going to the home page https://store.23andme.com/en-us<br>
Checks that we are the home page by find the href element<br>
Adds 3 Health + Ancestry packages and 2 Ancestry packages<br>
Enters a username for each package and clicks on the continue button<br>

---Shipping Page---<br>
Checks that we are in the shipping page by checking the url and shipping text on the page<br>
Populates every element with the appropriate information, firstname, lastname, address, email, phone etc.. and clicks on the continue button<br>

---Address Verification Page---<br>
Checks that we are in the verification page by checking the url and address verification text on the page<br>
Click on the 'ship to verified address' button<br>

---Billing Page---<br>
Checks that we are in the billing page by checking the url and billing text on the page<br>
Populate the elements in the page, like credit card number, expiration date and ccv code<br>
Clicks on the address option 'same as shipping'<br>
Click on the 'continue' button<br>

--Review Page---<br>
Checks that we are in the review page by checking the url and review text on the page<br>
Clicks on the 'I accept the Terms of Service'<br>
Clicks on the 'submit order' button<br>

---Check for Error---<br>
Checks if the page has an error message<br>
Currently this expects an error because it complains about the credit card number<br>


## Built With

PyCharm IDE

## Contributing


## Authors

Victor Magana

## License


## Acknowledgments

Many thanks and help from tutorials and online practice web pages from http://toolsqa.com/