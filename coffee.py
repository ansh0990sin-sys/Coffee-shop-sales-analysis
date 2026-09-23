import numpy as np
import pandas as pd

# 1. Create NumPy arrays
coffee_name = np.array([
    "Espresso",
    "Latte",
    "Cappuccino",
    "Mocha",
    "Cold Coffee"
])

cups_sold = np.array([120, 95, 150, 80, 110])

price_per_cup = np.array([120, 180, 160, 200, 150])

# 2. Create Pandas DataFrame
df = pd.DataFrame({
    "Coffee": coffee_name,
    "Cups Sold": cups_sold,
    "Price (₹)": price_per_cup
})

# 3. Display complete DataFrame
print("----- COFFEE SHOP SALES DATA -----")
print(df)

# 4. Create Revenue column
df["Revenue (₹)"] = df["Cups Sold"] * df["Price (₹)"]

# 5. Display updated DataFrame
print("\n----- UPDATED SALES DATA -----")
print(df)

# 6. Perform analysis

# Most Sold Coffee
most_sold = df.loc[df["Cups Sold"].idxmax(), "Coffee"]

# Most Expensive Coffee
most_expensive = df.loc[df["Price (₹)"].idxmax(), "Coffee"]

# Average Coffee Price
average_price = df["Price (₹)"].mean()

# Total Revenue
total_revenue = df["Revenue (₹)"].sum()

# 7. Display final sales report
print("\n========== COFFEE SHOP SALES REPORT ==========")
print("Most Sold Coffee       :", most_sold)
print("Most Expensive Coffee  :", most_expensive)
print("Average Coffee Price   : ₹", average_price)
print("Total Revenue Earned   : ₹", total_revenue)
print("==============================================")