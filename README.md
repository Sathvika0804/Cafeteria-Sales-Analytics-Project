🍽️📊 Cafeteria Sales Data Cleaning and Analysis

This project focuses on cleaning and analyzing cafeteria sales transaction data to uncover key patterns and propose strategies for increasing sales and revenue.

---

## 🎯 Project Objectives

* 🧹 Clean raw cafeteria sales data by handling missing, inconsistent, and duplicate records.
* 🔄 Convert data types and engineer a reliable **Total Spent** metric.
* 📈 Perform exploratory data analysis (EDA) to understand products, payment methods, time trends, and location preferences.
* 💡 Generate actionable business recommendations to improve revenue and customer experience.

---

## 📂 Dataset Overview

The dataset contains cafeteria transaction-level records with fields such as:

* 📅 Transaction Date
* 🍔 Item
* 🔢 Quantity
* 💲 Price Per Unit
* 🧮 Total Spent
* 💳 Payment Method
* 📍 Location

The goal is to transform this raw data into a clean, analysis-ready dataset and derive insights.

---

## 🧼 Data Cleaning Steps

Key cleaning operations performed:

* 🗓️ Converted `Transaction Date` to datetime and removed rows with invalid dates.
* ❓ Handled missing values for `Item`, `Quantity`, `Price Per Unit`, and `Total Spent` using defaults like **“Unknown”** and median values.
* 🧮 Recalculated `Total Spent` as `Quantity * Price Per Unit`.
* 🧽 Replaced inconsistent entries such as `UNKNOWN` and `ERROR`.
* 🔧 Cast `Quantity` to integer and price-related columns to float.
* 🚫 Removed duplicate records and refilled missing categorical values.
* 💾 Saved multiple cleaned versions:

  * `cleaned_cafeteria_sales.csv`
  * `cleaned_cafeteria_sales_v2.csv`
  * `cleaned_cafeteria_sales_final.csv`

---

## 🔍 Exploratory Data Analysis (EDA)

Using the cleaned data, the project explores:

* 🥇 **Best-selling products**
* 💰 **Revenue contribution** by premium items
* 💳 **Payment method trends**
* 📅 **Monthly sales patterns**
* 🏠 **Location preferences** (Dine-in vs Takeout)

Visualizations include:

* 📊 Bar charts
* 📈 Line charts
* 🥧 Pie charts

Created using **Matplotlib**.

---

## 💡 Key Insights

* ☕ Coffee, sandwiches, and juice drive the highest transaction volume.
* 🍕🍰 Pizza and cakes generate high revenue per sale despite lower volume.
* 💳 Cash and card dominate transactions; digital payments remain low.
* 📆 Mid-year months (July–October) see the highest sales; dips occur at the start and end of the year.
* 🥡 Takeout orders far exceed dine-in, stressing speed and packaging quality.

---

## 🚀 Business Recommendations

* 🍱 Combo deals (e.g., coffee + sandwich) and seasonal discounts during low-sales months.
* 🍕 Promote high-profit items like pizza and cakes through marketing and new variants.
* ⚡ Improve takeout processing speed and packaging quality.
* 🎁 Offer incentives for digital payments to encourage adoption.
* ⏰ Use transaction time data to run targeted offers like **Happy Hour** and **quick-lunch combos**.

---

## 🛠️ Tech Stack

* 🐍 Python
* 📦 Pandas & NumPy for data cleaning and preprocessing
* 📊 Matplotlib for visualizations

---

## ▶️ How to Run

1. 📥 Clone this repository.
2. 📦 Install required Python packages (use `requirements.txt`).
3. 📁 Place the raw dataset in the `data/` folder.
4. 🧹 Run the cleaning script/notebook to generate cleaned datasets.
5. 📊 Run the EDA notebook to reproduce visualizations and insights.

---

## 🙏 Acknowledgements

This project respects intellectual property and copyright.
The dataset and code are used strictly for **educational and analytical purposes**.

---
