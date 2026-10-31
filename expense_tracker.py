
import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses.")

    return []


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save expenses.")
        return False


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category (Food, Travel, etc.): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    note = input("Enter a short description: ").strip()

    expense = {
        "date": str(date.today()),
        "amount": round(amount, 2),
        "category": category,
        "note": note
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")
    else:
        expenses.pop()


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print("Date:", expense["date"])
        print("Amount: ₹", f'{expense["amount"]:.2f}')
        print("Category:", expense["category"])
        print("Description:", expense["note"])


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


def show_category_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = (
            summary.get(category, 0) + expense["amount"]
        )

    print("\n--- Category Summary ---")

    for category, amount in sorted(summary.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_category_summary(expenses)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()
