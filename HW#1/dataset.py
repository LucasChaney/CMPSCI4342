import pandas as pd
from datetime import datetime
from itertools import combinations
from collections import Counter


#Creat Map for Product Prices
product_prices = {
    201: 10.5,
    202: 20.3,
    203: 16.25,
    204: 18.1,
    205: 6.5,
    206: 25.00,
    207: 3.25,
    208: 9.99,
    209: 4.75,
    210: 5.3
}

# Create Dataset
data = {
    "TransactionID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "CustomerID": [101, 102, 103, 104, 105, 103, 106, 107, 108, 102],
    "ProductID": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Quantity": [5, 1, 6, 8, 2, 4, 9, 3, 5, 6],
    "Date": [
        datetime(2025, 1, 1),
        datetime(2025, 1, 2),
        datetime(2025, 1, 3),
        datetime(2025, 1, 4),
        datetime(2025, 1, 5),
        datetime(2025, 1, 6),
        datetime(2025, 1, 7),
        datetime(2025, 1, 8),
        datetime(2025, 1, 9),
        datetime(2025, 1, 10),
    ],
}

# Create a Class Called Transaction
class Transaction:
    def __init__(self,TransactionID,CustomerID,Date):
        self.TransactionID = TransactionID
        self.CustomerID = CustomerID
        self.Date = Date
        self.items = []

    def add_item(self,ProductID,Quantity):
        Price = product_prices.get(ProductID,0)
        self.items.append({
            "ProductID":ProductID,
            "Quantity":Quantity,
            "Price":Price
        })

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["Quantity"] * item["Price"]
        return total
    
    def display(self):
        print(f"TransactionID: {self.TransactionID}, CustomerID: {self.CustomerID}, Date: {self.Date}")
        for item in self.items:
            print(f"    ProductID: {item['ProductID']}, Quantity: {item['Quantity']}, Price: {item['Price']}")
        print(f"    Total Price: {self.total_price()}")


# Create a List of Transaction Objects
transactions = []
for i in range(len(data["TransactionID"])):
    transaction = Transaction(data["TransactionID"][i],data["CustomerID"][i],data["Date"][i])
    transaction.add_item(data["ProductID"][i],data["Quantity"][i])
    transactions.append(transaction)

transactions[0].add_item(ProductID=202,Quantity=2)
transactions[0].add_item(ProductID=203,Quantity=3)

#Display all transactions
print("Displaying Transactions")
for transaction in transactions:
    transaction.display()
    print("\n")

#Flatten Transactions Into a DataFrame
rows = []
for transaction in transactions:
    for item in transaction.items:
        rows.append({
            "TransactionID":transaction.TransactionID,
            "CustomerID":transaction.CustomerID,
            "Date":transaction.Date,
            "ProductID":item["ProductID"],
            "Quantity":item["Quantity"],
            "Price":item["Price"],
            "TotalPrice":item["Quantity"] * item["Price"]
        })

df = pd.DataFrame(rows)
print("\nFlattened DataFrame")
print(df)

# Total Transactions and Unique Customers
total_transactions = df["TransactionID"].nunique()
unique_customers = df["CustomerID"].nunique()
print(f"\nTotal Transactions: {total_transactions}")
print(f"Unique Customers: {unique_customers}")

# Total Revenue
total_revenue = df["TotalPrice"].sum()
print(f"Total Revenue: ${total_revenue:.2f}")

#Average Transaction total
average_transaction_total = df.groupby("TransactionID")["TotalPrice"].sum().mean()
print(f"Average Transaction Total: ${average_transaction_total:.2f}")

# Most Frequently Purchased Product
most_frequent_product = df.groupby("ProductID")["Quantity"].sum().idxmax()
most_frequent_quantity = df.groupby("ProductID")["Quantity"].sum().max()
print(f"Most Frequently Purchased Product: ProductID {most_frequent_product} with {most_frequent_quantity} units sold")

# Identify high-volume and low-volume buyers
customer_totals = df.groupby("CustomerID")["Quantity"].sum()
high_volume_threshold = customer_totals.quantile(0.60)
low_volume_threshold = customer_totals.quantile(0.40)

high_volume_customers = customer_totals[customer_totals > high_volume_threshold]
low_volume_customers = customer_totals[customer_totals <= low_volume_threshold]

print("\nHigh-volume customers:")
print(high_volume_customers)
print("\nLow-volume customers:")
print(low_volume_customers)

# Identify potential product bundling opportunities
product_pairs = []
for transaction_id in df["TransactionID"].unique():
    products = df[df["TransactionID"] == transaction_id]["ProductID"].tolist()
    product_pairs.extend(combinations(products, 2))

# Count frequent product pairs
pair_counts = Counter(product_pairs)
common_pairs = pair_counts.most_common(5)
print("\nTop product bundling opportunities:")
for pair, count in common_pairs:
    print(f"Products {pair} were purchased together {count} times")