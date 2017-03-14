# Selenium using Python scripts

Selenium using Python scripts showing basic interaction with a web page form

## Getting Started

The Selenium normal script fills out a web form by finding different web page elements such as text box, selects radio, checkbox, drop down options
Also goes thru a user registration process by finding different web page elements and veryfying by asserting at different points of the process
This file consist of two unit test one for filling out the form and other is the user registration

The Selenium page object script fills out a web form by finding different web page elements
Project breakdown:  
basePage.py - options shared by all web pages  
pageLocators.py - contains the elements locators per web page  
testCasesText.py - list which contains a test description  
pageObjects.py - has a method to access each element in the web page  
testPages.py - runs the unit test, each test interacts with one web page element using the same web browser instance  
Can be ran in specified order or default alphabetical order  

These test were verified on a Windows 7 with Firefox browser.

### Prerequisites

Python 2.7, Selenium Webdriver, gecko firefox driver

## Running the tests

Execute testPages.py

### Break down into the tests

Fill out web form elements like Username textboxes, Years of experience radio options, date, checkbox, drop down menu, multi select menu
and doing some asserts to check data is correct

## Built With

PyCharm IDE

## Contributing


## Authors


## License


## Acknowledgments

Many thanks and help from tutorials and online practice web pages from http://toolsqa.com/