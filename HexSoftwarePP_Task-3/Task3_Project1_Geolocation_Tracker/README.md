# 🌍 IP Geolocation Tracker using Python

## 📌 Project Overview

The IP Geolocation Tracker is a Python-based application that allows users to enter any valid IP address and retrieve its geographical location information. The application fetches details such as city, state, country, latitude, and longitude using a geolocation API and visualizes the location on an interactive map.

The generated map contains a marker indicating the detected location and is automatically opened in the user's web browser.

This project demonstrates the practical use of APIs, geolocation services, map visualization, and Python automation.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

* Retrieve location details using an IP address.
* Display geographical information in a structured format.
* Generate an interactive map showing the detected location.
* Learn API integration using Python.
* Understand geolocation tracking concepts.
* Visualize real-world location data.

---

## 🚀 Features

### 🌐 IP Address Lookup

* Accepts any valid public IP address as input.
* Retrieves location information in real time.

### 📍 Location Information

Displays:

* IP Address
* City
* State / Region
* Country
* Latitude
* Longitude

### 🗺️ Interactive Map

* Generates an HTML map using Folium.
* Places a marker at the detected location.
* Opens automatically in the browser.

### ⚡ Real-Time Tracking

* Fetches live geolocation data through an API.
* Provides quick and accurate location details.

---

## 🛠️ Technologies Used

* Python 3
* Requests
* Folium
* Webbrowser Module
* Geolocation API

---

## 📈 Project Workflow

### 1. User Input

* User enters a valid IP address.

### 2. API Request

* Send request to geolocation API.
* Retrieve location data.

### 3. Data Processing

Extract:

* City
* State
* Country
* Latitude
* Longitude

### 4. Map Generation

* Create interactive map.
* Add marker for detected location.

### 5. Display Results

* Show location details in terminal.
* Open generated map in browser.

---

## 📊 Sample Output

```text
===== IP Geolocation Tracker =====

Enter IP Address: 117.212.84.115

IP Address: 117.212.84.115
City: Rajkot
State: Gujarat
Country: India

Latitude: 22.2904
Longitude: 70.7915

Map Generated Successfully!
```

---

## 🗺️ Sample Map Output

The application generates:

```text
location_map.html
```

The map displays a location marker for the entered IP address.

Example Location:

```text
City: Rajkot
State: Gujarat
Country: India
```

---

## 🔍 Key Outcomes

* Successfully tracked location using IP addresses.
* Integrated geolocation API with Python.
* Generated interactive maps dynamically.
* Visualized geographical coordinates.
* Improved understanding of APIs and location services.

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

* Python Programming
* API Integration
* JSON Data Handling
* Geolocation Services
* Interactive Map Visualization
* Web Automation
* Data Processing
* Problem Solving

---

## ✅ Conclusion

This project demonstrates the implementation of an IP Geolocation Tracker using Python. By integrating a geolocation API and map visualization tools, the application can identify the geographical location of a given IP address and display it interactively on a map.

The project provides practical experience in working with APIs, location-based services, and Python automation.

---

## 📦 Requirements

Install required libraries:

```bash
pip install requests folium
```

---

## 📂 Project Structure

```text
Task3_Project1_Geolocation_Tracker/
│
├── geolocation_tracker.py
├── location_map.html
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── output.png
    └── map_output.png
```


---

## 🚀 Run Project

```bash
python geolocation_tracker.py
```


---

## 📸 Screenshots

### Terminal Output

Displays:

* Entered IP Address
* City
* State
* Country
* Latitude
* Longitude

### Browser Map Output

Displays:

* Interactive OpenStreetMap
* Marker indicating detected location

---

## 👨‍💻 Author

**Armi Sherathiya**

Hex Softwares Python Programming Project