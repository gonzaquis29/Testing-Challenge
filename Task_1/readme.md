# UI Automated Test

This project contains an automated test for https://demo.evershop.io/ using Selenium WebDriver and Python.

## Prerequisites

- Python 3.7 or higher
- Git

## Setup

1. You must be in Task_1 directory, then you must install the required packages by using the following command:

   `pip install selenium pytest faker webdriver-manager`

## Running the Test

To run the test, execute the following command:

`pytest -s`

## Project Structure

- `tests/`: Contains the test files
- `pages/`: Contains the Page Object Model classes
- `utils/`: Contains utility functions for test data generation
- `conftest.py`: Contains pytest configuration
- `requirements.txt`: Lists the project dependencies

## Additional Libraries Used

- **Selenium WebDriver**: Used for browser automation
- **pytest**: Testing framework for running the tests
- **Faker**: Library for generating fake data for test inputs
- **webdriver_manager**: Automatically manages WebDriver binaries

## Notes

- The test uses Chrome as the default browser. So it is important to make sure Chrome installed on your system.
- The test generates random customer data for each run, ensuring unique test cases. However, there could be cases in which an account with the given consumer data exists. In such case, it is recommended to execute the test again.
