"""class Ticket:
    def __init(self, pass_name, bag_weight):
        self.pass_name = pass_name
        self.bag_weight = bag_weight

    def display_info(self):
        return f"{self.pass_name} is carrying a bag that weighs {self.bag_weight} Kgs"

    def add_pass_info(new_pass, new_bag_weight):
        pass_names = ['Fidelis', 'Kim', 'Mkuruu']
        new_pass = input("Enter a new passengers name: ").strip()
        if new_pass.isalpha:
            pass_names.append(new_pass)
            return f"The new passanger {new_pass} has been added to the passengers list: {pass_names}"
        else:
            print("Invalid input of new passengers name!")
        exit()

        bag_weight = [25, 42, 16]
        pass_bag = dict(zip(pass_names, bag_weight))


passengers = {}
names = ["Fidel", "Divine"]
Grades = ["80", "70"]
passengers = dict(zip(names, Grades))
print(passengers)
"""


'''
class Tickets:
    def __init__(self):
        self.passengers = dict(zip(passenger_names, bag_weights))

class EconomyPassenger(Tickets):
        super().__init__()

    def add_pass(self):
        no_of_pass = int(input("Enter the number of passengers you want to add: "))
        pass_count = len(self.passengers)
        for num in range(no_of_pass):
            pass_count += 1
            passenger_name = input("Enter the name of the new passenger: ").strip()
            new_bag_weight = int(input("Enter the weight of the bag that the passenger is carrying: "))
            print("")
            self.passengers[passenger_name] = new_bag_weight

        print(f"The total number of passengers is {pass_count}")
        print("==============================================================================")
        print("")
        print(f"added {no_of_pass} passenger(s) successfully")

    def show_pass(self):
        if not self.passengers:
            print("The passengers list is empty")
        else:
            for name, weight in self.passengers.items():
                print(f"{name} has a bag weighing {weight} Kgs")
        print("")
        print(self.passengers)

passenger_names = ('Tom', 'Ben', 'Ken', 'Martin')
bag_weights = (45, 16, 94, 77)

if __name__ == '__main__':
    tickets_sys = Tickets()
    tickets_sys.add_pass()
    tickets_sys.show_pass()
'''
from datetime import datetime
class Booking:
    def __init__(self, name, current_location, destination, date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        return f"The passenger name is {self.name} and is currently at {self.current_location} heading to {self.destination} on {self.date}"
    def get_weight_allowance(self):
        return

class EconomyPassenger(Booking):
    def __init__(self, name, current_location, destination, date):
        super().__init__(name, current_location, destination, date)
    def get_passenger_info(self):
        return f"The passenger name is {self.name} and is currently at {self.current_location} heading to {self.destination} on {self.date}"

class FirstClassPassenger(Booking):
    def __init__(self, name, current_location, destination, date, weight, lounge_access):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.lounge_access = lounge_access

    def get_passenger_info(self):
        return (f"The passenger name is {self.name} and is currently at {self.current_location} heading to {self.destination} on {self.date}."
                f" The passengers weight is {self.weight} and ")

    def set_weight(self):
        weight = int(input("Enter the weight of the passenger: "))
        self.weight = weight
        return self.weight
    def access_lounge(self):
        access = input("Does the passenger have access to lounge? (yes/no)").strip().lower()

        if access == 'yes':
            self.lounge_access = True
            return self.lounge_access
        elif access == 'no':
            self.lounge_access = False
            return self.lounge_access
        else:
            print("Invalid input!")
            exit()


class PremiumPassenger(Booking):
    def __init__(self, name, current_location, destination, date, weight, priority_boarding):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding




passenger1 = Booking('Fidelis', 'Kigali', 'Nairobi', f'{datetime.now()}')

if __name__ == '__main__':

    print(passenger1.get_passenger_info())
    print(passenger1.get_weight_allowance())
    #print(passenger1.access_lounge())













