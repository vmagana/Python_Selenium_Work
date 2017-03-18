# Selenium using Python scripts

Selenium using Python scripts showing basic interaction to fill out a basic user form

## Getting Started

This project is done using Page Objects so its easier to maintain by modifying page elements if needed without rewriting much code.
The Selenium Python script fills out a user web form by interacting with different elements on the web page.
Asserts are done after interacting with every element.

## Project breakdown
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
Fills out a user web form by interacting with different web page elements

## Built With

PyCharm IDE

## Contributing


## Authors

Victor Magana

## License


## Acknowledgments

Many thanks and help from tutorials and online practice web pages from http://toolsqa.com/