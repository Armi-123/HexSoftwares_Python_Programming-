import pandas as pd
import os

FILE_NAME = "HexSoftwarePP_Task-2/Task2_Project2_Expense_Tracker/expenses.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Amount", "Category", "Description"])
    df.to_csv(FILE_NAME, index=False)

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        description = input("Enter Description: ")

        new_expense = pd.DataFrame({
            "Amount": [amount],
            "Category": [category],
            "Description": [description]
        })

        new_expense.to_csv(FILE_NAME, mode="a", header=False, index=False)

        print("Expense Added Successfully!")

    elif choice == "2":
        data = pd.read_csv(FILE_NAME)
        print("\nExpenses List")
        print(data)

    elif choice == "3":
        data = pd.read_csv(FILE_NAME)

        print("\nExpense Summary")
        print(data.groupby("Category")["Amount"].sum())

        print("\nTotal Expense:", data["Amount"].sum())

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")