#Design a class hierarchy for a library system. Create a base class called Book with attributes title, author, and isbn.
#Implement a derived class called EBook that adds an attribute for file_size and overrides a method get_info() to include the file size in the output.
# Create instances of both Book and EBook and demonstrate how the information is retrieved.
'''
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
Implement a class hierarchy for a vehicle management system.
 Create a base class called Vehicle with attributes make, model, and year. 
 Then, create two derived classes: Car and Truck. 
 The Car class should have an additional attribute num_doors,
  while the Truck class should have an additional attribute payload_capacity.
  Both derived classes should override a method vehicle_info() to provide detailed information about the vehicle.
   Finally, create a list of vehicles (both cars and trucks) 
   and demonstrate polymorphism by iterating through the list and calling the vehicle_info() method on each vehicle.

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
'''

from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year, rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        return total
class Car(Vehicle):
    def __init__(self, make, model, year, rental_price, num_doors):
        super().__init__(make, model, year, rental_price)
        self.num_doors = num_doors
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Number of Doors: {self.num_doors}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        if days > 7:
            total *= 0.9
            return total
        else:
            return self.rental_price

class Truck(Vehicle):
    def __init__(self, make, model, year, rental_price, payload_capacity):
        super().__init__(make, model, year, rental_price)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Payload Capacity: {self.payload_capacity}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        if days < 3:
            total += 20.00
            return total
        else:
            return self.rental_price

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, rental_price, engine_size):
        super().__init__( make, model, year, rental_price)
        self.engine_size = engine_size
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Engine Size: {self.engine_size}"

    def calculate_rental_cost(self, days):
        total = self.rental_price
        total = 15.0 * days
        return total


class RentalSystem:
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.customer_dict = {'fidel':9854, 'mwiti':32122, 'Moreen':546542 }
        self.rented_vehicles = {'fidel': (), 'mwiti': (), 'Moreen': ()}

    def add_customer(self):
        customer_count = len(self.customer_dict)
        no_of_customers = int(input("Enter the number of customers you would like to add: "))
        for customer in range(no_of_customers):
            name = input("Enter the name of the customer: ").strip()
            license_number = int(input("Enter the customer's license number: "))
            self.customer_dict[name] = license_number
            self.rented_vehicles[name] = ()
            print(f"The new customer's name is: {name} and their license number is: {license_number} ")
            customer_count += 1
        print(self.customer_dict)
        print("")
        return self.customer_dict


    def rent_vehicle(self):
       name = input("Enter the name of the customer: ").strip()
       if not name or not self.customer_dict[name]:
           print(f"Customer does not exist. Kindly add the new customer.")
           exit()
       else:
           print("Customer exists.")

       number_of_vehicles = input("Enter the number of vehicles you wish to rent: ").strip()
       try:
           number_of_vehicles = int(number_of_vehicles)
       except ValueError:
           print("Invalid input. Please enter a valid number")
           exit()
       rented = ()
       for i in  range(number_of_vehicles):
           model = input("Enter the model of the vehicle you want to rent: ").strip()
           if not model or not self.vehicles:
               print("Vehicle does not exist in our inventory. Enter a correct vehicle model.")
               exit()
           else:
               print("Vehicle exists in our inventory and is ready for hire.")

           days = int(input("Enter the number of days you wish to rent the vehicle: "))
           new_rented = rented + (model, days)
           self.rented_vehicles[name] = new_rented
           print(f"You have successfully rented the following vehicles: {self.rented_vehicles[name]}")
       print({self.rented_vehicles[name]})
       return self.rented_vehicles
















    def return_vehicle(self, vehicle):
        customer_returning = input("Enter the name of the customer returning the vehicle: ").strip()
        if not customer_returning or not Customer.get_customer_info(self):
            print(f"The customer {customer_returning} does not exist in the customers list. Kindly confirm the name entered. ")
            exit()
        else:
            vehicle = input("Enter the make of the vehicle you wish to return: ").strip().lower()
            if vehicle in self.rented_vehicles:
                self.rented_vehicles.remove(vehicle)
                print(f"{vehicle} has been returned by {customer_returning} on {datetime.now()}")
            else:
                print("Invalid vehicle make input. Kindly check the make of the vehicle again.")
                exit()
        return self.rented_vehicles

    def get_rental_summary(self): #A method to write the summary of all rented vehicles with their costs
                name = input("Enter the name of the customer to see their rental summary: ").strip()
                if not name or not self.customer_dict:
                    print("Invalid customer name entered or customer does not exist!")
                    exit()
                else:
                    print(f"{name} has rented the following vehicles: {self.customer_dict[name]}")
                    for vehicle in self.customer_dict[name]:
                        print(f"{vehicle} has a rental price of: ${Vehicle.rental_price}")
                return self.customer_dict[name]

        
vehicles = [
    Truck("ford", "f-150", 2021, 50.0, "2000lbs"),
    Motorcycle("harley_Davidson", "sportster", 2022, 20.0, "600cc"),
    Car("toyota", "camry", 2020, 40.0, 4)
]

if __name__ == "__main__":
    RentalSystem = RentalSystem(vehicles)
    #RentalSystem.add_customer()
    RentalSystem.rent_vehicle()
