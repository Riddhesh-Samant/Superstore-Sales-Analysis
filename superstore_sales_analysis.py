import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\riddh\\OneDrive\\Desktop\\vs python\\Sample - Superstore.csv", encoding='ISO-8859-1')

# Print first 10 values from the dataset
print(df.head(10))
# Print all the column names

print(df.columns)

# Which region generates the highest sales and profit

print(df.groupby("Region")[["Sales","Profit"]].sum())

# Which product categories are most profitable

print(df.groupby('Category')['Profit'].sum())

# Which sub-categories are causing losses

print(df.groupby('Sub-Category')['Profit'].sum().sort_values())

# Does giving higher discounts reduce profit

print(df.groupby("Discount")["Profit"].mean().sort_values())

# Which customer segment is most valuable

print(df.groupby('Segment')['Profit'].sum())

# Top 10 customers by sales

print(df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(10))

# Does higher quantity lead to higher profit

print(df['Quantity'].corr(df['Profit']))

# Identify loss-making orders

loss_orders = df[df["Profit"] < 0][["Order ID", "Profit"]]

print(loss_orders)

# Sales by Category (Bar Chart)

category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(kind='bar',title= 'Sales by category')
plt.ylabel('Sales')
plt.show()

# Profit by Sub-Category (Bar Chart)

Sub_category_profit = df.groupby('Sub-Category')['Profit'].sum()

Sub_category_profit.plot(kind = 'bar',title = 'Profit by Sub-Category')
plt.ylabel('Profit')
plt.show()
# Quantity vs Profit (Scatter Plot)

plt.scatter(df['Quantity'],df['Profit'])
plt.xlabel('Quantity')
plt.ylabel('Profit')
plt.title('Quantity vs Profit')
plt.grid(True)
plt.show()










