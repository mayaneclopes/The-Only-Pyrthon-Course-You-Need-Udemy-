# You're preparing an order summary with customer names and their total bill.
# Tasks:
# 1. Use two lists: one for names, and one for bills.
# 2. Print [Name] paid $[amount]

names = ["Maria", "José", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} dolars")