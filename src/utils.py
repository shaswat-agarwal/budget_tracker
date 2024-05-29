# src/utils.py
import csv


def export_to_csv(transactions, file_name="transactions_export.csv"):
    try:
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Category", "Amount", "Date"])
            for transaction in transactions:
                writer.writerow(
                    [
                        transaction["type"],
                        transaction["category"],
                        transaction["amount"],
                        transaction["date"],
                    ]
                )
        print(f"Data exported to {file_name}")
    except Exception as e:
        print(f"Error exporting data: {e}")
