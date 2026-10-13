import pandas as pd

data = {
    "customer": ["A", "B", "C", "D", "E"],
    "amount": [120, 450, 80, 700, 250],
    "transactions": [5, 12, 3, 15, 8]
}

df = pd.DataFrame(data)

print("Full dataset:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nSummary statistics:")
print(df.describe())

print("\nAverage transaction amount:")
print(df["amount"].mean())

print("\nCustomers with amounts above RM 200:")
print(df[df["amount"] > 200])
