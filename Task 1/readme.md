# UI Automated Test

This project contains an automated test for https://demo.evershop.io/ using Selenium WebDriver and Python.

## Prerequisites

- Python 3.7 or higher
- Git

## Setup

1. Clone the repository:
   git clone

2. Create and activate a virtual environment:
   python -m venv venv
   Then execute this command in Windows:
   venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

## Running the Test

To run the test, execute the following command:
pytest -s

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

- The test uses Chrome as the default browser. So it is important to ,make sure Chrome installed on your system.
- The test generates random customer data for each run, ensuring unique test cases.
