#ENCAPSULATION
#Involves bundling of data or attributes or fields and methods and behaviours that operates in a data in a single unit called a class
#It helps in hiding the internal implementation details in a class by only exposing the necessary functionalities to the outside world

class BadBankAccount:#A bad bank account where the user can change their account balances at will
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = 4854458
print(account.balance)
#A good bank functional bank account
class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount has to be positive")
        self._balance += amount
        return self._balance
    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount has to be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        return self.balance

account = BankAccount()
print(f"initial account balance is: ${account.balance}")
print(f"The account balance after the deposit is: ${account.deposit(12)}")

print(f"The account balance after the withdrawal is: ${account.withdrawal(11)}")

#Abstraction
#Reduce complexity by hiding unnecessary details.
class EmailService:
    def send_email(self):
        # Call private methods within the class
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server...")


email = EmailService()
email.send_email()

# LOGS:
# Sending email...
# Connecting to email server...
# Authenticating...
# Disconnecting from email server...

#BAD EMAIL SERVICE
class BadEmailService:
    # def send_email(self):
    #     self.connect()
    #     self.authenticate()
    #     print("Sending email...")
    #     self.disconnect()

    def connect(self):
        print("Connecting to email server...")

    def authenticate(self):
        print("Authenticating...")

    # We could also force clients to call connect, authenticate, send_email, and disconnect to send an email. That wouldn't be very nice tho! No abstraction means more effort for client/dev.
    def send_email(self):
        print("Sending email...")

    def disconnect(self):
        print("Disconnecting from email server...")

email = BadEmailService()

email.connect()
email.authenticate()
email.send_email()
email.disconnect()

# LOGS:
# Connecting to email server...
# Authenticating...
# Sending email...
# Disconnecting from email server...

# Oh no, I don't have such a simple API to just send an email (this thing I actually want to do). Much easier to make mistakes -- I might forget to disconnect after sending.
# What happens if implementation details change? Client code has to change.


#INHERITANCE
#Inheritance is a fundamental concept in object-oriented programming(OOP) that involves creating new classes (subclasses or derived classes) based on existing classes(super classes or base classes)

