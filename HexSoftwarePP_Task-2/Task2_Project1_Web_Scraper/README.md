# 🌐 Web Scraper using Python

## 📌 Project Overview

The Web Scraper Project is a Python-based application that extracts data from websites and stores it in a structured format for analysis and further processing.

This project demonstrates how to collect information from web pages using Python libraries such as **Requests**, **BeautifulSoup**, and **Pandas**. The extracted data is cleaned and saved into CSV files for easy access and analysis.

As part of this project, data was scraped from sample websites and stored in structured datasets.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

- Extract data from websites automatically.
- Parse HTML content using BeautifulSoup.
- Store scraped information in CSV format.
- Practice web scraping techniques using Python.
- Understand website structure and HTML elements.
- Organize extracted data into a structured dataset.

---

## 🚀 Features

### 📥 Data Extraction

- Connects to websites using HTTP requests.
- Downloads webpage content for processing.

### 🔍 HTML Parsing

- Extracts specific information from HTML pages.
- Identifies elements using tags and classes.

### 📊 Structured Data Storage

- Saves extracted information into CSV files.
- Creates datasets suitable for analysis.

### ⚡ Automated Collection

- Eliminates manual data collection.
- Retrieves multiple records efficiently.

---

## 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas

---

## 📈 Project Workflow

### 1. Send Request

- Connect to the target website.
- Retrieve webpage content.

### 2. Parse HTML

- Load webpage source code.
- Locate required HTML elements.

### 3. Extract Information

For Books Website:

- Book Title
- Price
- Rating

For Quotes Website:

- Quote
- Author

### 4. Create Dataset

- Store extracted information in Pandas DataFrames.

### 5. Export Results

- Save data into CSV files.

---

## 📊 Scraped Datasets

### 📚 Books Dataset

Extracted Fields:

- Book Title
- Price
- Rating

Output File:

```text
books_data.csv
```

### 💬 Quotes Dataset

Extracted Fields:

- Quote
- Author

Output File:

```text
output.csv
```

---

## 📷 Sample Output

### Books Data

```text
Book Title                              Price    Rating
A Light in the Attic                    £51.77   Three
Tipping the Velvet                      £53.74   One
Soumission                              £50.10   One
Sharp Objects                           £47.82   Four
Sapiens: A Brief History of Humankind   £54.23   Five
```

### Quotes Data

```text
Quote                                      Author
The world as we have created it...         Albert Einstein
It is our choices, Harry...                J.K. Rowling
There are only two ways to live your life  Albert Einstein
```

---

## 📁 Output Files

```text
books_data.csv
output.csv
```

These files contain the structured data extracted from the websites.

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

- Python Programming
- Web Scraping
- HTML Parsing
- Data Extraction
- Data Cleaning
- CSV File Handling
- Pandas Data Analysis
- BeautifulSoup Usage

---

## 🔍 Key Outcomes

- Successfully connected to websites.
- Extracted structured information from HTML pages.
- Generated CSV datasets automatically.
- Automated data collection process.
- Improved understanding of web technologies and scraping techniques.

---

## ✅ Conclusion

This project demonstrates the implementation of a Web Scraper using Python. By leveraging Requests, BeautifulSoup, and Pandas, useful information was collected from websites and stored in structured datasets.

The project highlights practical applications of automation, data extraction, and data management, making it a valuable introduction to web scraping and data collection techniques.

---

## 📦 Requirements

Install required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

---

## 📂 Project Structure

```text
Task2_Project1_Web_Scraper/
│
├── web_scraper.py
├── Book_web_scraper.py
├── books_data.csv
├── output.csv
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── Book_scrap.png
    └── Web_scrap.png
```

---

## 🚀 Run Project

### Quotes Scraper

```bash
python web_scraper.py
```

### Books Scraper

```bash
python Book_web_scraper.py
```

---

## 👨‍💻 Author

**Armi Sherathiya**

Hex Softwares Python Programming Project