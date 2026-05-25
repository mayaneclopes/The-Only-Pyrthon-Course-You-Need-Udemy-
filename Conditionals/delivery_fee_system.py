# You run an online tea shop store.
# If the order amount is more than $300, delivery is free
# otherwise it costs $30. 
# Tasks:
# 1. Input: order_amount
# 2. Use ternary operator to decide delivery fee.

order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fee is: {delivery_fees}")