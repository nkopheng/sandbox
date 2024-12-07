from rich.traceback import install
install(show_locals=True)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

# Create an instance of Person
person = Person(name, age, address)

# Display the information
print("\nUser Information:")
person.display_info()
