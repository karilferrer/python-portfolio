expenses = []


def add_expense():
    expense = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    expenses.append({
        "expense": expense,
        "amount": amount
    })

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\nExpenses List:")
    for expense in expenses:
        print(f"Expense: {expense['expense']} | Amount: {expense['amount']}")


def search_expense():
    name = input("Enter expense name: ")

    for expense in expenses:
        if expense["expense"].lower() == name.lower():
            print("\nExpense Found")
            print(f"Name: {expense['expense']}")
            print(f"Amount: {expense['amount']}")
            return

    print("Expense not found.")


def calculate_expense():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: {total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Calculate Total Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expense()

    elif choice == "4":
        calculate_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")