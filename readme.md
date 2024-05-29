# Personal Budget Tracker

## Overview

The Personal Budget Tracker is a console-based application that allows users to manage their expenses and income. It provides features for tracking transactions, calculating the remaining budget, analyzing expenses, and exporting data.

## Features

- **Add Transactions**: Input income and expenses with categories and amounts.
- **Delete Transactions**: Remove specific transactions.
- **View Budget**: Calculate and display the remaining budget.
- **Analyze Expenses**: Categorize expenses and display spending trends.
- **View All Transactions**: Display all recorded transactions.
- **Export Data**: Export transaction data to a CSV file.
- **Data Persistence**: Store transactions in a JSON file for tracking over time.

## Setup Instructions

1. **Clone the repository**:

   ```sh
   git clone https://github.com/shaswat-agarwal/budget_tracker.git
   ```

2. **Navigate to the project directory**:

   ```sh
   cd budget_tracker
   ```

3. **Create the `data` directory and an empty `budget_data.json` file**:

   ```sh
   mkdir data
   echo "[]" > data/budget_data.json
   ```

4. **Run the application**:
   ```sh
   python main.py
   ```

## Usage Guide

1. **Main Menu**:

   - Choose an option from the main menu by entering the corresponding number:
     1. Add Income
     2. Add Expense
     3. View Budget
     4. Analyze Expenses
     5. View All Transactions
     6. Delete Transaction
     7. Export Data to CSV
     8. Exit

2. **Add Income**:

   - Enter the income category and amount when prompted.

3. **Add Expense**:

   - Enter the expense category and amount when prompted.

4. **View Budget**:

   - Displays the remaining budget after deducting expenses from income.

5. **Analyze Expenses**:

   - Categorizes and displays total spending for each expense category.

6. **View All Transactions**:

   - Lists all recorded transactions with their details.

7. **Delete Transaction**:

   - View all transactions and enter the index of the transaction to delete.

8. **Export Data to CSV**:

   - Exports all transaction data to a CSV file named `transactions_export.csv`.

9. **Exit**:
   - Exit the application.

## Error Handling

- The application includes error handling to manage invalid inputs and unexpected errors gracefully. Users are prompted with meaningful error messages in case of issues.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality of the Personal Budget Tracker.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
