import numpy as np

transaction_amounts = np.array([120, 450, 80, 700, 250])

print("Amounts:", transaction_amounts)
print("Total:", np.sum(transaction_amounts))
print("Average:", np.mean(transaction_amounts))
print("Maximum:", np.max(transaction_amounts))
print("Minimum:", np.min(transaction_amounts))

# Add a 10% fee to every amount
with_fee = transaction_amounts * 1.10
print("Amounts with fee:", with_fee)

print(transaction_amounts[transaction_amounts > 200])
