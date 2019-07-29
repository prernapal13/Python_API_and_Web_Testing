# Relayr Assignment

## Description
This framework supports automation testing of APIs and UI both. For testing API endpoints, python's requests, json & jsonpath modules is being used. And for testing UI, selenium webdriver is being used along with python unittest framework. 
Page Object Model(POM) is used to make the code more readable, maintainable, and reusable. Test reports are being generated using nose-html-reporting module. In case of any UI test case failure, framework supports taking snapshot of screen on which failure occured.

- Answers for task 1 are available at [Solution_Task1.pdf](https://github.com/prernapal13/relayr_assignment/blob/master/Solution_Task1.pdf)
- Manual test cases(task 2 and task 2 alternative) are available in [TestCases_Task2.xlsx](https://github.com/prernapal13/relayr_assignment/blob/master/TestCases_Task2.xlsx)

## Pre-Requisites:
1. Python (version 2.7)
2. requests module(pip install requests)
3. jsonpath module (pip install jsonpath)
4. nose-html-reporting module(pip install nose-html-reporting)
5. Selenium (pip install selenium==3.141.0)
6. Google Chrome (version 74.0.3729.131)
7. Google Chrome Browser drivers
8. PyCharm or any other desired IDE

## Automation Flow:
### API Tests:
Automated test cases related to public APIs available on https://reqres.in
1. Verify GET request for returning single user returns queried user with status code 200
2. Verify POST request for creating new user returns status code 201 along with user details
3. Verify PUT request for updating existing user returns status code 200 along with user details
4. Verify DELETE request for deleting existing user should return status code 204 

### UI Tests: 
Automated test cases related to Google search functionality
1. Verify google home page
2. Verify search results contain search keyword
3. Verify 'did you mean' functionality of google search
4. Verify 'No search result found'  functionality

## How to Execute:
1. Please run below command to execute API test cases:
	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases\api_tests.py`
2. Please run below command to execute UI test cases:
	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases\google_search_tests.py`
3. Please run below command to execute all test cases:
	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases`

## Execution
![Execution](https://github.com/prernapal13/relayr_assignment/blob/master/screenshots/execution.gif)

## Report Snapshot
![Report Snapshot](https://github.com/prernapal13/relayr_assignment/blob/master/screenshots/execution_report_snapshot.PNG)
