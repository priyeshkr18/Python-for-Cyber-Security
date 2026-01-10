class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self):
        acc_no = input("Enter account number: ")
        if acc_no in self.accounts:
            print("Account already exists")
            return
        name = input("Enter name: ")
        balance = float(input("Enter initial deposit: "))
        self.accounts[acc_no] = {"name": name, "balance": balance}
        print("Account created successfully")

    def deposit(self):
        acc_no = input("Enter account number: ")
        if acc_no not in self.accounts:
            print("Account not found")
            return
        amount = float(input("Enter deposit amount: "))
        self.accounts[acc_no]["balance"] += amount
        print("Deposit successful")
        print("Current Balance:", self.accounts[acc_no]["balance"])


bank = Bank()

while True:
    print("\n1. Open Account")
    print("2. Deposit")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        bank.open_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
