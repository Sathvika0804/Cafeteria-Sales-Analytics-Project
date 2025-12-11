import pandas as pd
import numpy as np
'''
data = pd.read_csv("C:/Users/sathv/Downloads/upload_664b9ce1-c0e2-43cc-ba4d-6a6b22d9d2c8.csv")
#print(data)
print(data.info())
print(data.describe())
#print(data.to_string())

#Identify and handle missing values in key fields such as transaction date,
#item, quantity, or price per unit

# 1. Transaction Date
# Convert to datetime
data['Transaction Date'] = pd.to_datetime(data['Transaction Date'], errors='coerce')
print("Missing dates:", data['Transaction Date'].isna().sum())
data = data.dropna(subset=['Transaction Date'])

print("Missing items:", data['Item'].isna().sum())
data['Item'] = data['Item'].fillna("Unknown Item")


data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
data['Price Per Unit ($)'] = pd.to_numeric(data['Price Per Unit ($)'], errors='coerce')

# Fill missing Quantity with median
median_qty = data['Quantity'].median()
data['Quantity'] = data['Quantity'].fillna(median_qty)

# Fill missing Price with median
median_price = data['Price Per Unit ($)'].median()
data['Price Per Unit ($)'] = data['Price Per Unit ($)'].fillna(median_price)

# Recalculate Total Spent ($)
data['Total Spent ($)'] = data['Quantity'] * data['Price Per Unit ($)']

print(" Missing values handled!")
print(data.isna().sum())  
print(data.info())
print(data.describe())

data.to_csv("cleaned_cafeteria_sales.csv", index=False)
print(" File saved as cleaned_cafeteria_sales.csv")

#Correct incorrect or inconsistent entries
#(entries containing UNKNOWN, ERROR)

# Loading the latest cleaned file
data = pd.read_csv("cleaned_cafeteria_sales.csv")
# 1. Handle incorrect values (UNKNOWN, ERROR)
# Replace 'UNKNOWN' and 'ERROR' with NaN
data = data.replace(["UNKNOWN", "ERROR"], pd.NA)

#Convert data types to appropriate formats (e.g., integers for quantity,
#floats for price, datetime for timestamp).

# 2. Convert data types
# Convert Quantity to integer
data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce").astype("Int64")

# Convert Price Per Unit to float
data["Price Per Unit ($)"] = pd.to_numeric(data["Price Per Unit ($)"], errors="coerce")

# Convert Total Spent to float
data["Total Spent ($)"] = pd.to_numeric(data["Total Spent ($)"], errors="coerce")

# Convert Transaction Date to datetime
data["Transaction Date"] = pd.to_datetime(data["Transaction Date"], errors="coerce")

# 3. Save the cleaned file
data.to_csv("cleaned_cafeteria_sales_v2.csv", index=False)

# 4. Print quick check
print(data.dtypes)
print("File saved as cleaned_cafeteria_sales_v2.csv")
print(data.describe())
print(data.info())

#Remove duplicate records 
#glitches or repeated data entries

# Loading the latest cleaned file
data = pd.read_csv("cleaned_cafeteria_sales_v2.csv")

# 1. Remove duplicate records
print("Duplicates before:", data.duplicated().sum())
data = data.drop_duplicates()
print("After removing duplicates:", data.shape)

# 2. Fill missing values
data['Item'] = data['Item'].fillna("Unknown")
data['Payment Method'] = data['Payment Method'].fillna("Unknown")
data['Location'] = data['Location'].fillna("Not Provided")

# 3. Re-checking the missing values
print("\nMissing values after cleaning:")
print(data.isna().sum())

#Find correlation, if any between data columns

# 4. Correlation check
print("\nCorrelation between numeric columns:")
print(data[['Quantity', 'Price Per Unit ($)', 'Total Spent ($)']].corr())

# 5. Saving the final cleaned file
data.to_csv("cleaned_cafeteria_sales_final.csv", index=False)
print("\n Final cleaned file saved as 'cleaned_cafeteria_sales_final.csv'")

print(data.info())
print(data.describe())
#print(data.to_string())

'''
import pandas as pd
import matplotlib.pyplot as plt

# Loaded the  cleaned data
df = pd.read_csv("cleaned_cafeteria_sales_v2.csv")

# --- 1. Top Selling Items ---
top_items = df['Item'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_items.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Top 10 Selling Items")
plt.xlabel("Item")
plt.ylabel("Number of Sales")

plt.show()

# --- 2. Revenue by Item ---
revenue_by_item = df.groupby('Item')['Total Spent ($)'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
revenue_by_item.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Top 10 Revenue Generating Items")
plt.xlabel("Item")
plt.ylabel("Total Revenue ($)")

plt.show()

# --- 3. Payment Method  ---
payment_counts = df['Payment Method'].value_counts()
plt.figure(figsize=(6,6))
payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold','skyblue','lightcoral'])
plt.title("Payment Method Distribution")
plt.ylabel("")  # removes y-label
plt.show()

# --- 4. Sales Over Time ---
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
sales_over_time = df.groupby(df['Transaction Date'].dt.to_period("M"))['Total Spent ($)'].sum()
sales_over_time.plot(kind='line', marker='o', figsize=(10,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# --- 5. Location Preference ---
location_counts = df['Location'].value_counts()
plt.figure(figsize=(6,5))
location_counts.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Sales by Location")
plt.xlabel("Location")
plt.ylabel("Number of Sales")

plt.show()


