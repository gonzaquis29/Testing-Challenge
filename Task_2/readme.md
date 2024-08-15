# Testing APIs

This project contains an automated test for https://api.countrylayer.com/v2/all and https://api.countrylayer.com/v2/alpha/{code}

## Prerequisites

- Python 3.7 or higher
- Git

## Setup
Install the required packages:
`pip install requests`

## Running the Test

To run the test, execute the following command:
`python api_tests.py`

## Libraries Used

- **requests**: Used for making HTTP requests and validating APIs work as expected

## Notes

- The api_tests.py contains key, it is recommended to change the API KEYS with your own API KEY as it has a limit of requests.