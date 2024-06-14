### Summary

This repository stores the autotests on Python that I created for an online bookstore.
The bookstore was a fake website used for testing while taking the training course.  

### Instruction
- clone the repository to your computer
- create a virtual environment to run the tests if necessary 
```
python3 -m venv venv
````
- use the `requirements.txt` file to install the required pacakges 
```
pip3 install -r requirements.txt
```
 
### Project Description
Tests are written and organised in accordance with the POM principles. 
Below is the description of the files. 

#### "Pages" folder:
`base_page.py` - includes methods that provide basic functionality

`basket_page.py` - includes methods for interacting with the elements of the basket/cart page

`locators.py` - includes all locators that are used throughout the project 

`login_page.py` - includes methods for the login page

`main_page.py` - includes methods for the main page

`product_page.py` - includes methods for the product page


#### Root folder:
`__init__.py` - imports

`conftest.py` - fixture to start a browser before the tests execution

`pytest.ini` - markers for tests

`requirements.txt` - the list of the dependencies (external libraries and packages) 

#### Tests:
`test_main_page.py` - autotests for the main page

`test_product_page.py` - autotests for the product page
