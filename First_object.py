class Car: #creating a class that contains the cars and their attributes
    Car_count = 0 #static attribute for the class Car which counts the number of objects on the init method

    def __init__(self, name, company, model, DOM, Owner):#defining the attributes of the objects
        self.name = name
        self.company = company
        self.model = model
        self.DOM = DOM
        self.Owner = Owner
        Car.Car_count += 1


class Owner: #initiating a class that contains the object(owner) attributes
    def __init__(self, name, address, contact, nationality):
        self.name = name
        self.address = address
        self.contact = contact
        self.nationality = nationality

owner1 = Owner('Moreen', 'Bumbogo KG31', 254113205350, 'Kenya')
car1 = Car('R8', 'audi', '2020 model', 2020, owner1)
print(car1.name, car1.company, car1.model, end=': ')
print(car1.Owner.name, car1.Owner.address, car1.Owner.contact, car1.Owner.nationality)
print('====================================================')

owner2 = Owner('Fide', 'Meru - 60200', 254112277621, 'Russia')
car2 = Car('Phantom', 'RollsRoys', '2022 model', 2022, owner2)
print(car2.name, car2.company, car2.model, end=': ')
print(car2.Owner.name, car2.Owner.address, car2.Owner.contact, car2.Owner.nationality)
print(Car.Car_count)


from datetime import datetime
class Person:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password

    def get_email(self):
        print(f"The email was accessed at: {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        new_email = input("Enter the new email: ").strip().lower()
        if "@" and "." in new_email:
            self._email = new_email
            return self._email
        else:
            print("Invalid email input. Enter a correct email")
            exit

user1 = Person("Fidelis", "f.mwiti@alustudent.com", '12345')
print(f"The old email is: {user1.get_email()}")
print(f"The new email is: {user1.set_email(new_email=str)}")

from datetime import datetime
class Person:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password
    @property
    def email(self):
        print(f"The email was accessed at: {datetime.now()}")
        return self._email
    @email.setter
    def email(self, new_email):
        if "@" and "." in new_email:
            self._email = new_email
            return self._email
user1 = Person("Fidelis", "f.mwiti@alustudent.com", '12345')
user1.email = 'kamtuu@gmail.com'
print(user1.email)



class BankAccount:
    MIN_BALANCE = 100
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def withdrawal(self, amount):
        if self._is_amount_valid(amount):
            self.balance -= amount
            self.__log_transaction('withdrawal', amount)
            print(f"{self.owner}'s new account balance is: ${self.balance}")
            return self.balance
        else:
            print("Amount cannot be negative")
            exit()
    def _is_amount_valid(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(f"The {transaction_type} of ${amount} was successfully made")

    @staticmethod
    def is_rate_valid(rate):
        return 0 <= rate <= 5

account = BankAccount('Fidel', 500)
account.withdrawal(100)
print(BankAccount.is_rate_valid(2.5))
print(BankAccount.is_rate_valid(-1))


from datetime import datetime
class students:
    MIN_GRADE = 1
    def __init__(self, name, email, grade, parent):
        self.name = name
        self._email = email
        self.grade = grade
        self.parent = parent

    @property
    def email(self):
        print(F"Email was accessed at: {datetime.now()}")
        return self._email
    @email.setter
    def email(self, new_email):
        if '@' and '.' in new_email:
            self._email = new_email
            print("New email loaded successfully")
            return self._email
        else:
            print("Invalid input: Please enter a valid input")
            exit()

class parent:
    def __init__(self, parent_name, contact, address):
        self.parent_name = parent_name
        self.contact = contact
        self.address = address

parent1 = parent('Mwiti', '+254112277621', '1839-60200 Meru, Kenya')
parent2 = parent('Kamon','+250795456636', 'Bumbogo KG432, Kigali' )

student1 = students('Fidel', 'f.mwiti@alustudent.com', 86, parent1)
student2  = students('Kamtuu', 'kamtuu@gmail.com',75, parent2)

student1._email = 'mwitifidelis3@gmail.com'
student2._email = 'kamtuu@alustudent.com'
print(f"{student1.name} changed their emails at {datetime.now()} to the new email: {student1.email}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"{student2.name} changed their emails at {datetime.now()} to the new email: {student2.email}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"My name is {student1.name} and I was able to attain a percentage of {student1.grade} in my exams. My parents name is {student1.parent.parent_name} and lives in {student1.parent.address}. My parent's contact is: {student1.parent.contact}")
print("======================================================================")
print(f"My name is {student2.name} of email {student2.email} and i got grade {student2.grade} in my exams. My parent, {student2.parent.parent_name}, was very exited and called the facilitator on her contact: {student2.parent.contact}")
print("======================================================================")
