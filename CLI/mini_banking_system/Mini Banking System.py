accounts = []


def create_account():
    name = input("Enter account name: ")
    
    accounts.append({
        'name' : name,
        'balance' : 0
    })

    print("Account created successfully!")

def view_account():
    if len(accounts) == 0:
        print("No accounts found")
        return
    
    print("==== ACCOUNTS ====")

    for account in accounts:
        print(f"Name: {account['name']}")
        print(f"Balance: {account['balance']}")

    
def deposit():
    name = input("Enter account name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    for account in accounts:
        if account["name"].lower() == name.lower():

            account["balance"] += amount

            print("Deposit successful!")
            print(f"New Balance: {account['balance']}")
            return

    print("Account not found.")

def withdraw():
    name = input("Enter account name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    for account in accounts:
        if account["name"].lower() == name.lower():

            if account['balance'] < amount:
                print("Insufficient funds")
                return

            else:
                account["balance"] -= amount

                print("Withdrawal successful!")
                print(f"New Balance: {account['balance']}")
                return

    print("Account not found.")


def check_balance():
    account_name = input("Enter account name: ")
    for account in accounts:
        if account['name'].lower() == account_name.lower():
            print("Account Found!")
            print(f"Name: {account['name']}")
            print(f"Balance: {account['balance']}")
            return
        
    print("Account Not Found")


while True:
    print("==== MINI BANKING SYSTEM ====")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()

    elif choice == '2':
        view_account()

    elif choice == '3':
        deposit()

    elif choice == '4':
        withdraw()
    
    elif choice == '5':
        check_balance()

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")