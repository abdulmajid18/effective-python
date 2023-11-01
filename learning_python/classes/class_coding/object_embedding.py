class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city} - {self.zip_code}"


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee:
    def __init__(self, person, address, employee_id):
        self.person = person
        self.address = address
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee ID: {self.employee_id}\n" \
               f"Name: {self.person}\n" \
               f"Address: {self.address}"


# Create Address and Person objects
home_address = Address("123 Main St", "Anytown", "12345")
john_doe = Person("John", "Doe")

# Compose an Employee object using Address and Person
employee = Employee(john_doe, home_address, "E12345")

# Print the Employee object
print(employee)
