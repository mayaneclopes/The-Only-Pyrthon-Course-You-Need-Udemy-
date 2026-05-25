# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Tasks:
# 1. Input: small, medium, large
# 2. Small: $10, Medium: $15, Large: 20
# 3. If invalid: show "Unkown cup size"

size = input("Choose your cup size (small/medium/large): ").lower()

if size == "small":
    print("Price is $10")
elif size == "medium": 
    print("Price is $15")
elif size == "large":
    print("Price is $20")
else:
    print("Unknown cup size")