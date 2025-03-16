class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public member
        self.__balance = balance     # Private member

    # Public method to access balance
    def get_balance(self):
        print(f'Available Balance :{self.__balance}')

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance is {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}, new balance is {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")


while True:
    obj_account = BankAccount("Amit", 10000)
    choice=int(input('Select an option...\n1. Balance Enquiry\n2. Withdraw Money\n3. Deposit Money\n4. Exit\n'))
    if choice==1:
        obj_account.get_balance()    # Access the private attribute through a public method
    elif choice==2:
        amount=int(input('Enter amount to withdraw : '))
        obj_account.withdraw(amount) 
    elif choice==3:
        amount=int(input('Enter amount to deposit : '))
        obj_account.deposit(amount)
    else:
        print('Your transaction has been completed ')
        break           

# Direct access to private variable will raise an error:
# print(obj_account.__balance)  # This will raise an AttributeError