import requests
import time

# Constants for API key and URL
API_KEY = "aae6513a138997e18b017627c34aec8e"
BASE_URL = "https://api.countrylayer.com/v2"


def test_get_country(country_code):
    url = f"{BASE_URL}/alpha/{country_code}?access_key={API_KEY}"
    response = requests.get(url)
    print(f"Get {country_code} with status Code: {response.status_code}")
    # Status code 200 means 
    if response.status_code == 200:
        print(f"Country: {response.json()['name']}")
    else:
        print("Response from server: ", response.text)
        print("It was not possible to get the name of the country")


def test_inexistent_country():
    inexistent_country_code = "XXYXYA"
    url = f"{BASE_URL}/alpha/{inexistent_country_code}?access_key={API_KEY}"
    response = requests.get(url)
    print(f"Get Inexistent Country with status Code: {response.status_code}")

    if response.status_code == 404:
        print("Inexistent country (As expected)")
    else:
        print("Response:", response.text)
        print("It was expected to get a 404 status code")

def test_post_new_country():
    url = f"{BASE_URL}/all?access_key={API_KEY}"
    data = {
        "name": "CountryTest",
        "alpha2_code": "CT",
        "alpha3_code": "CTT"
    }
    response = requests.post(url, json=data)
    print(f"POST New Country with status Code: {response.status_code}")

    if response.status_code == 500:
        print("Something went wrong with the server. It means POST is not allowed (as expected)")
    else:
        print("Response:", response.text)
        print("Unexpected response or error in POST request")

# Run all the tests
# Notice there are time.sleep() because there are rate limits per request with the API

print("Testing existing countries:\n")
for country in ["US", "DE", "GB"]:    
    test_get_country(country)
    # Must add some time to avoid rate limit errors
    time.sleep(2)

print("\n\nTesting inexistent country:")
time.sleep(2)
test_inexistent_country()

print("\n\nTesting POST Method and try to add a new country:")
time.sleep(2)
test_post_new_country()