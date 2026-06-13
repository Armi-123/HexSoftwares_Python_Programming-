print("===== Rent Calculator =====")

rent = float(input("Enter Total Rent: ₹"))
electricity = float(input("Enter Electricity Bill: ₹"))
food = float(input("Enter Food Expenses: ₹"))
persons = int(input("Enter Number of Persons: "))

total_expense = rent + electricity + food
per_person = total_expense / persons

print("\n===== Rent Summary =====")
print("Total Expense: ₹", total_expense)
print("Number of Persons:", persons)
print("Rent Per Person: ₹", round(per_person, 2))