import pandas as pd
from datetime import datetime

# Create dataset
data = {
    "TransactionID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "CustomerID": [101, 102, 103, 104, 105, 103, 106, 107, 108, 102],
    "ProductID": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Quantity": [5, 1, 6, 8, 2, 4, 9, 3, 5, 6],
    "Price": [10.5, 20.3, 16.25, 18.1, 6.5, 25.00, 3.25, 9.99, 4.75, 5.3],
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

df = pd.DataFrame(data)

# Display the dataset
print("Dataset:")
print(df)
