# src/transaction_manager.py
import os
import json
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/budget_data.json")


class TransactionManager:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as file:
                    self.transactions = json.load(file)
            else:
                self.transactions = []
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump(self.transactions, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_transaction(self, type, category, amount):
        try:
            transaction = {
                "type": type,
                "category": category,
                "amount": amount,
                "date": str(datetime.now()),
            }
            self.transactions.append(transaction)
            self.save_data()
        except Exception as e:
            print(f"Error adding transaction: {e}")

    def delete_transaction(self, index):
        try:
            if 0 <= index < len(self.transactions):
                del self.transactions[index]
                self.save_data()
            else:
                print("Invalid index.")
        except Exception as e:
            print(f"Error deleting transaction: {e}")

    def get_all_transactions(self):
        return self.transactions
