# 💰 Expense Tracker using Python

## 📌 Project Overview

The Expense Tracker is a Python-based application that helps users record, organize, and analyze their daily expenses. Users can add expenses, categorize spending, view saved records, and generate expense summaries.

This project demonstrates the use of Python for financial tracking, data management, and basic data analysis. Expense records are stored in a CSV file, making it easy to maintain and review spending habits.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

- Track daily expenses efficiently.
- Categorize expenses for better organization.
- Store expense records in a structured format.
- Generate spending summaries.
- Improve financial management and budgeting skills.
- Practice file handling and data analysis using Python.

---

## 🚀 Features

### ➕ Add Expense

Users can enter:

- Expense Amount
- Expense Category
- Expense Description

Example:

```text
Amount: 500
Category: Food
Description: Weekend Dinner
```

### 📋 View Expenses

Displays all recorded expenses in a tabular format.

### 📊 Expense Summary

Provides:

- Category-wise expense totals
- Overall expense total

### 💾 CSV Storage

All expense records are automatically saved in:

```text
expenses.csv
```
---

## 🛠️ Technologies Used

- Python 3
- Pandas
- CSV File Handling

---

## 📈 Project Workflow

### 1. Add Expense

- Enter amount.
- Enter category.
- Enter description.
- Save expense to CSV file.

### 2. View Expenses

- Read data from CSV.
- Display all expense records.

### 3. Generate Summary

- Group expenses by category.
- Calculate total expenses.
- Display category-wise spending.

### 4. Exit Application

- Safely close the program.

---

## 📊 Sample Output

### Add Expense

```text
===== Expense Tracker =====

1. Add Expense
2. View Expenses
3. Expense Summary
4. Exit

Enter choice: 1

Enter Amount: 500
Enter Category: Food
Enter Description: Weekend Dinner

Expense Added Successfully!
```

### View Expenses

```text
Expenses List

Amount  Category  Description
500.0   Food      Weekend Dinner
```

### Expense Summary

```text
Expense Summary

Category
Food    500.0

Total Expense: 500.0
```
---

## 📁 Output File

```text
expenses.csv
```

Example:

```csv
Amount,Category,Description
500,Food,Weekend Dinner
```

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

- Python Programming
- File Handling
- CSV Data Storage
- Data Analysis using Pandas
- User Input Validation
- Financial Data Management
- Console-Based Application Development

---

## 🔍 Key Outcomes

- Successfully recorded expenses.
- Generated category-wise spending summaries.
- Stored data in CSV format.
- Improved understanding of data organization.
- Developed a simple personal finance management system.

---

## ✅ Conclusion

This project demonstrates how Python can be used to build a simple yet effective Expense Tracker. The application allows users to manage expenses, categorize spending, and generate useful summaries for better financial awareness.

The project provides practical experience in file handling, data storage, and basic analytics using Python and Pandas.

---

## 📦 Requirements

Install required library:

```bash
pip install pandas
```

---

## 📂 Project Structure

```text
Task2_Project2_Expense_Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── Output.png
   
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