import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")

# Calculate total spending per category
category_totals = df.groupby("category")["amount"].sum()

# Create a bar chart
category_totals.plot(kind="bar")

plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (RM)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
