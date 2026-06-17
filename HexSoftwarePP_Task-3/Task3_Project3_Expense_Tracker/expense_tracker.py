import pandas as pd
import os
from datetime import datetime

FILE_NAME = "HexSoftwarePP_Task-3/Task3_Project3_Expense_Tracker/expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(
        columns=["Date", "Amount", "Category", "Description"]
    )
    df.to_csv(FILE_NAME, index=False)


def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    expense = pd.DataFrame({
        "Date": [date],
        "Amount": [amount],
        "Category": [category],
        "Description": [description]
    })

    expense.to_csv(
        FILE_NAME,
        mode="a",
        header=False,
        index=False
    )

    print("\n✅ Expense Added Successfully!")


def view_expenses():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Expenses Found!")
    else:
        print("\n===== Expenses List =====")
        print(df)


def expense_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Expenses Available!")
        return

    print("\n===== Category Summary =====")
    print(df.groupby("Category")["Amount"].sum())

    print("\nTotal Expense:", df["Amount"].sum())


def monthly_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Expenses Available!")
        return

    print("\n===== Monthly Expense Summary =====")
    print(df.groupby("Date")["Amount"].sum())


def main():

    while True:

        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_summary()

        elif choice == "4":
            monthly_summary()

        elif choice == "5":
            print("\nThank You!")
            break

        else:
            print("\n❌ Invalid Choice!")


if __name__ == "__main__":
    main()