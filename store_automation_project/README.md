# Selenium Store Checkout Automation using Python scripts

Selenium using Python scripts showing basic interaction during a store checkout web form

## Getting Started

This project is done so it can be maintained pretty easy by modify page elements if needed without rewriting much code.
There could be timing issues that need to be fined tuned due to delays in response from web pages.
The Selenium page object script fills out a web forms by finding different web page elements.
Asserts are done after interacting with every element, main checks are counter values, url of page and error messages.
There could be more checks at every element like comparing text values after entering them, dollar amount total for items being ordered.
This checkout web page can be driven from information in a file and used to populate the page.

## Project breakdown:
basePage.py - options shared by all web pages  
pageLocators.py - contains the elements locators per web page  
pageObjects.py - has a method to access each element in the web page  
testPages.py - runs the unit test, each test interacts with one web page element using the same web browser instance  
Can be ran in specified order or default alphabetical order  

These test were verified on a Windows 7 with Firefox browser.  

### Prerequisites

Python 2.7, Selenium Webdriver, gecko firefox driver, python selenium webdriver

## Running the tests

Execute testPages.py

### Break down into the tests
---Home Page---  
Starts by opening up a firefox browser instance and going to the home page https://store.23andme.com/en-us  
Checks that we are the home page by find the href element  
Adds 3 Health + Ancestry packages and 2 Ancestry packages  
Enters a username for each package, verifies the counter has the correct value and clicks on the continue button

---Shipping Page---  
Checks that we are in the shipping page by checking the url and shipping text on the page<br>
Populates every element with the appropriate information, firstname, lastname, address, email, phone etc.. and clicks on the continue button  

---Address Verification Page---  
Checks that we are in the verification page by checking the url and address verification text on the page  
Click on the 'ship to verified address' button  

---Billing Page---  
Checks that we are in the billing page by checking the url and billing text on the page  
Populate the elements in the page, like credit card number, expiration date and ccv code  
Clicks on the address option 'same as shipping'  
Click on the 'continue' button  

--Review Page---  
Checks that we are in the review page by checking the url and review text on the page  
Clicks on the 'I accept the Terms of Service'  
Clicks on the 'submit order' button  

---Check for Error---  
Checks if the page has an error message  
Currently this expects an error because it complains about the credit card number  


## Built With

PyCharm IDE

## Contributing


## Authors

Victor Magana

## License


## Acknowledgments

Many thanks and help from tutorials and online practice web pages from http://toolsqa.com/