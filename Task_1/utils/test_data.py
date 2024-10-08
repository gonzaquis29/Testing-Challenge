from faker import Faker

# Create an object to generate fake data to make tests.
fake = Faker()

def generate_customer_data():
    return {
        'full_name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'telephone': fake.phone_number(),
        'address_1': fake.street_address(),
        'city': fake.city(),
        'postcode': fake.postcode()
    }

