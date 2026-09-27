expenses = []

categories = {
    "Food",
    "Travel",
    "Education",
    "Entertainment",
    "Shopping",
    "Other"
}

monthly_budget = 0

def add_expense():
    print("\n========== ADD EXPENSE ==========")

    name = input("Enter expense name: ")

    amount = float(input("Enter amount: ₹"))

    print("\nAvailable Categories:")
    for category in categories:
        print("-", category)

    category = input("Enter category: ").title()

    if category not in categories:
        print("Invalid category. Expense added under 'Other'.")
        category = "Other"

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("\nExpense added successfully!")

def display_expenses():
    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\nNo.  Expense              Amount       Category")
    print("-----------------------------------------------")

    count = 1

    for expense in expenses:
        print(
            count,
            "  ",
            expense["name"],
            " " * max(1, 20 - len(expense["name"])),
            "₹", expense["amount"],
            "   ",
            expense["category"]
        )

        count += 1

def total_spending():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\n========== TOTAL SPENDING ==========")
    print("Total amount spent: ₹", total)

    return total

def category_spending():
    print("\n========== CATEGORY-WISE SPENDING ==========")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for category in categories:

        total = 0

        for expense in expenses:

            if expense["category"] == category:
                total = total + expense["amount"]

        if total > 0:
            print(category, ": ₹", total)

def highest_expense():
    print("\n========== HIGHEST EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Expense :", highest["name"])
    print("Amount  : ₹", highest["amount"])
    print("Category:", highest["category"])

def lowest_expense():
    print("\n========== LOWEST EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    lowest = expenses[0]

    for expense in expenses:

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("Expense :", lowest["name"])
    print("Amount  : ₹", lowest["amount"])
    print("Category:", lowest["category"])

def search_expense():
    print("\n========== SEARCH EXPENSE ==========")

    search = input("Enter expense name to search: ").lower()

    found = False

    for expense in expenses:

        if search in expense["name"].lower():

            print("\nExpense :", expense["name"])
            print("Amount  : ₹", expense["amount"])
            print("Category:", expense["category"])

            found = True

    if found == False:
        print("No matching expense found.")

def set_budget():
    global monthly_budget

    print("\n========== SET MONTHLY BUDGET ==========")

    monthly_budget = float(
        input("Enter your monthly budget: ₹")
    )

    print("Monthly budget set to ₹", monthly_budget)

def check_budget():
    print("\n========== BUDGET STATUS ==========")

    if monthly_budget == 0:
        print("Monthly budget has not been set.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    remaining = monthly_budget - total

    print("Monthly Budget :", "₹", monthly_budget)
    print("Total Spent    :", "₹", total)

    if remaining > 0:

        print("Remaining      :", "₹", remaining)
        print("Status         : Within Budget")

    elif remaining == 0:

        print("Remaining      : ₹0")
        print("Status         : Budget Fully Used")

    else:

        print("Overspent      : ₹", abs(remaining))
        print("Status         : Budget Exceeded")

def display_categories():
    print("\n========== EXPENSE CATEGORIES ==========")

    for category in categories:
        print("-", category)

while True:

    print("\n")
    print("========================================")
    print("       COLLEGE EXPENSE TRACKER")
    print("========================================")

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Category-wise Spending")
    print("5. Find Highest Expense")
    print("6. Find Lowest Expense")
    print("7. Search Expense")
    print("8. Set Monthly Budget")
    print("9. Check Budget Status")
    print("10. Show Expense Categories")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        display_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        category_spending()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        lowest_expense()

    elif choice == "7":
        search_expense()

    elif choice == "8":
        set_budget()

    elif choice == "9":
        check_budget()

    elif choice == "10":
        display_categories()

    elif choice == "11":
        print("\nThank you for using College Expense Tracker!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")