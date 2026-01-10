class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name not in accounts:
            accounts[name] = BankAccount(name)
            print("Account created")
        else:
            print("Account already exists")

    elif choice == "2":
        name = input("Enter name: ")
        if name in accounts:
            amount = float(input("Enter amount: "))
            accounts[name].deposit(amount)
            print("Amount deposited")
        else:
            print("Account not found")

    elif choice == "3":
        name = input("Enter name: ")
        if name in accounts:
            amount = float(input("Enter amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found")

    elif choice == "4":
        name = input("Enter name: ")
        if name in accounts:
            accounts[name].show_balance()
        else:
            print("Account not found")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
