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

