# 🛠 Automated Product Registration Script
Welcome to the Automated Product Registration Script project! This Python script utilizes pyautogui to automate the registration of products on a web-based platform. The script opens a browser, logs into the platform, imports a product list from a CSV file, and automates the process of entering product data.

## 🧐 Overview
This script automates repetitive tasks, including logging into a platform and registering multiple products by reading a CSV file containing product information. It simplifies the task by interacting with the system through automation tools like pyautogui.

## ⚙️ Features
Automated Login: Logs into a web-based platform using a username and password.
Product Registration: Registers products from a CSV file, including fields like product code, brand, type, category, price, cost, and observations.
Data Automation: Uses pyautogui to enter data in a structured and efficient manner, reducing manual input errors.
Scrolling Automation: Automatically scrolls the page after entering each product to prepare for the next one.

## 💻 Technologies Used
Python: Main programming language used for automation.
pyautogui: Library used for GUI automation, controlling mouse movements and keyboard inputs.
pandas: Library used to read and manage the product data in CSV format.

## 🖥 How to Use
**Setup:**
_Ensure Python is installed on your machine._
**Install necessary libraries:**
_pip install pyautogui pandas_
_Ensure you have a produtos.csv file in the same directory as your script. This file should contain the product information to be registered._
**Run the script:**
_python automated_product_registration.py_

The script will automatically open Microsoft Edge, log into the system, and start registering products from the CSV file.
Wait for the process:
The script runs with a delay (time.sleep) to simulate human interaction and ensure each step is completed properly.

## 💡 How it Works
Step 1: Opens the Microsoft Edge browser and navigates to the login page.
Step 2: Logs into the platform using pre-defined credentials.
Step 3: Reads the produtos.csv file containing product data.
Step 4: Loops through each row of the CSV file, entering product information into the web form.
Step 5: Scrolls to the next page and repeats the process for all products.

##📐 Features in Action
Data Entry Automation: Saves hours of manual data entry by automating the entire product registration process.
Customization: Easily modify the script to suit different platforms or data fields.

## 💌 Credits
Special thanks to Hashtag Programação for providing the course and materials that made this automation possible!
