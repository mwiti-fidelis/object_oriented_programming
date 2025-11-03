#Design a class hierarchy for a library system. Create a base class called Book with attributes title, author, and isbn.
#Implement a derived class called EBook that adds an attribute for file_size and overrides a method get_info() to include the file size in the output.
# Create instances of both Book and EBook and demonstrate how the information is retrieved.

class Book:
    def __init__(self,title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        "Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 9780743273565"

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, File Size: {self.file_size}"

kitabu = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565')
ifukuu = EBook('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', '5MB')

print(kitabu.get_info())
print(ifukuu.get_info())
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"{kitabu.__dict__}")
print(f"{ifukuu.__dict__}")
print("=============================================================================================")
print("")


#example 2
'''Implement a class hierarchy for a vehicle management system.
 Create a base class called Vehicle with attributes make, model, and year. 
 Then, create two derived classes: Car and Truck. 
 The Car class should have an additional attribute num_doors,
  while the Truck class should have an additional attribute payload_capacity.
  Both derived classes should override a method vehicle_info() to provide detailed information about the vehicle.
   Finally, create a list of vehicles (both cars and trucks) 
   and demonstrate polymorphism by iterating through the list and calling the vehicle_info() method on each vehicle.
'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


    def vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Doors: {self.num_doors}"


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super(). __init__(make, model, year)
        self.payload_capacity = payload_capacity

    def vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Payload Capacity: {self.payload_capacity}"

Vehicle1 = Car("Toyota", "Camry", 2020, 4)
Vehicle2 = Truck("Ford", "F-150", 2021, "2000 lbs")

print(Vehicle1.vehicle_info())
print(Vehicle2.vehicle_info())

from datetime import datetime
class Vehicle:
    def __init__(self, make, model, year, rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}"

class Car(Vehicle):
    def __init__(self, make, model, year, rental_price, num_doors):
        super().__init__(make, model, year, rental_price)
        self.num_doors = num_doors
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Number of Doors: {self.num_doors}"

    def calculate_rental_cost(self, days):
        if days > 7:
            amount = self.rental_price * 0.1
            self.rental_price -= amount
            return self.rental_price
        else:
            return self.rental_price

class Truck(Vehicle):
    def __init__(self, make, model, year, rental_price, payload_capacity):
        super().__init__(make, model, year, rental_price)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Payload Capacity: {self.payload_capacity}"

    def calculate_rental_cost(self, days):
        if days < 3:
            amount = 20.0
            self.rental_price += amount
            return self.rental_price
        else:
            return self.rental_price

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, rental_price, engine_size):
        super().__init__( make, model, year, rental_price)
        self.engine_size = engine_size
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Engine Size: {self.engine_size}"

    def calculate_rental_cost(self):
        self.rental_price = 15.0
        return self.rental_price


class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle):
        self.rented_vehicles.append(vehicle)
        print(f"{vehicle.get_info()} has been rented to {self.name} on {datetime.now()}")

    def return_vehicle(self, vehicle):
        if vehicle in self.rented_vehicles:
            self.rented_vehicles.remove(vehicle)
            print(f"{vehicle.get_info()} has been returned by {self.name} on {datetime.now()}")
        
    def get_rental_summary(self, ):
                price = self.calculate_rental_price()
                for vehicle in self.rented_vehicles:
                    return f"{vehicle.get_info()} was rented at a cost of {price}"
        
Vehicles = [
    Truck("Ford", "F-150", 2021, 50.0, "2000lbs"),
    Motorcycle("Harley_Davidson", "Sportster", 2022, 20.0, "600cc"),
    Car("Toyota", "Camry", 2020, 40.0, 4)
]
