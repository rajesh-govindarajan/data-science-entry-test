# Assuming Car class is already defined as:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Create an instance:
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method:
my_car.describe_car()
