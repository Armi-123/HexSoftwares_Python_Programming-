# 💰 Personal Expense Tracker Using Python

## 📌 Project Overview

The Personal Expense Tracker is a Python-based console application that helps users record, manage, and analyze their daily expenses.

Users can add expenses, categorize spending, view all expense records, generate category-wise summaries, and calculate total expenses. All expense data is stored in a CSV file for future access and analysis.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

* Track daily personal expenses.
* Categorize expenses for better financial management.
* Store expense records in CSV format.
* Generate expense summaries.
* Calculate total spending.
* Analyze monthly expenses.
* Improve data management and reporting skills.

---

## ✨ Features

### ➕ Add Expense

Users can add:

* Amount
* Category
* Description
* Date (Automatically Generated)

Example:

```text
Amount: 2000
Category: Food
Description: Dinner
```

---

### 📋 View Expenses

Displays all stored expense records.

```text
Date        Amount  Category  Description
09-06-2026  2000    Food      Dinner
09-06-2026  7000    Rent      Home Rent
```

---

### 📊 Expense Summary

Shows category-wise expense totals.

Example:

```text
Food    2000
Rent    7000
```

---

### 📅 Monthly Summary

Displays expense totals grouped by date.

```text
09-06-2026    9000
```

---

### 💵 Total Expense Calculation

Automatically calculates overall spending.

```text
Total Expense: 9000
```

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* CSV File Handling

---

## 📈 Project Workflow

### 1. Create CSV Storage

* Create expense file if it does not exist.
* Store all expenses in CSV format.

### 2. Add Expenses

* Accept user inputs.
* Save records to CSV.

### 3. View Expense Records

* Load data from CSV.
* Display all expenses.

### 4. Generate Reports

* Category-wise summary.
* Monthly expense summary.
* Total expense calculation.

### 5. Exit Program

* Safely close application.

---

## 📷 Sample Output

```text
===== PERSONAL EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Expense Summary
4. Monthly Summary
5. Exit

Enter Choice: 1

Enter Amount: 2000
Enter Category: Food
Enter Description: Dinner

Expense Added Successfully!

-----------------------------------

Enter Choice: 2

Date        Amount  Category  Description
09-06-2026  2000    Food      Dinner
09-06-2026  7000    Rent      Home Rent

-----------------------------------

Enter Choice: 3

Food    2000
Rent    7000

Total Expense: 9000
```

---

## 🔍 Key Outcomes

* Successfully implemented expense management system.
* Integrated CSV-based data storage.
* Generated category-wise expense reports.
* Calculated total expenses automatically.
* Implemented monthly expense analysis.
* Improved data handling and reporting skills.

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

* Python Programming
* File Handling
* CSV Data Storage
* Pandas Library
* Data Analysis
* Expense Management
* Report Generation
* Problem Solving

---

## ✅ Conclusion

This project demonstrates how Python can be used to build a practical expense management application.

By storing expenses in CSV files and generating summaries, users can better understand their spending habits and manage personal finances more effectively.

The project showcases important concepts such as data storage, data analysis, file handling, and user interaction.

---

## 📦 Requirements

Install required package:

```bash
pip install pandas
```

---

## 📂 Project Structure

```text
Task3_Project3_Expense_Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── README.md
├── requirements.txt
│
└── screenshots/
    └── output.png
```

---

## 🚀 Run Project

```bash
python expense_tracker.py
```

---

## 👨‍💻 Author

**Armi Sherathiya**

Hex Softwares Python Programming Project


