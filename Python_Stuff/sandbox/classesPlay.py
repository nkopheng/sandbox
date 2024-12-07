from rich.traceback import install
install(show_locals=True)

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display_address(self):
        return f"{self.street}, {self.city}, {self.zip_code}"


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address  # Address object is passed here

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.display_address()}")


# Create an Address object
street = input("Enter street: ")
city = input("Enter city: ")
zip_code = input("Enter zip code: ")
address = Address(street, city, zip_code)

# Create a Person object
name = input("Enter your name: ")
age = input("Enter your age: ")
person = Person(name, age, address)

# Display information
print("\nUser Information:")
person.display_info()
