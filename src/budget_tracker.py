# src/budget_tracker.py
from .transaction_manager import TransactionManager
from .utils import export_to_csv


class BudgetTracker:
    def __init__(self):
        self.manager = TransactionManager()

    def calculate_budget(self):
        try:
            income = sum(
                t["amount"] for t in self.manager.transactions if t["type"] == "income"
            )
            expenses = sum(
                t["amount"] for t in self.manager.transactions if t["type"] == "expense"
            )
            return income - expenses
        except Exception as e:
            print(f"Error calculating budget: {e}")
            return 0

    def analyze_expenses(self):
        try:
            categories = {}
            for t in self.manager.transactions:
                if t["type"] == "expense":
                    categories[t["category"]] = (
                        categories.get(t["category"], 0) + t["amount"]
                    )

            for category, amount in categories.items():
                print(f"Category: {category}, Total Spent: {amount}")
        except Exception as e:
            print(f"Error analyzing expenses: {e}")

    def view_transactions(self):
        try:
            for idx, transaction in enumerate(self.manager.transactions):
                print(
                    f"{idx}. {transaction['type'].capitalize()} - {transaction['category']}: {transaction['amount']} (Date: {transaction['date']})"
                )
        except Exception as e:
            print(f"Error viewing transactions: {e}")

    def main_menu(self):
        while True:
            print("\nPersonal Budget Tracker")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Budget")
            print("4. Analyze Expenses")
            print("5. View All Transactions")
            print("6. Delete Transaction")
            print("7. Export Data to CSV")
            print("8. Exit")
            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    category = input("Enter income category: ")
                    amount = float(input("Enter amount: "))
                    self.manager.add_transaction("income", category, amount)
                elif choice == "2":
                    category = input("Enter expense category: ")
                    amount = float(input("Enter amount: "))
                    self.manager.add_transaction("expense", category, amount)
                elif choice == "3":
                    budget = self.calculate_budget()
                    print(f"Remaining Budget: {budget}")
                elif choice == "4":
                    self.analyze_expenses()
                elif choice == "5":
                    self.view_transactions()
                elif choice == "6":
                    self.view_transactions()
                    index = int(input("Enter the index of the transaction to delete: "))
                    self.manager.delete_transaction(index)
                elif choice == "7":
                    export_to_csv(self.manager.transactions)
                elif choice == "8":
                    print("Exiting Budget Tracker.")
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input. Please enter the correct value.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
