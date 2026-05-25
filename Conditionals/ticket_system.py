# You're building a ticket system for a railway app.
# Based on seat type, show its features.
# Tasks: 
# 1. Input: sleeper, AC, general, luxury
# 2. Match using match-case
# 3. Unknown -> show: Invalid seat type

seat_type = input("Enter seat type (sleeper/AC/general/luxury) ").lower()

match seat_type: 
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury": 
        print("Luxury - Premium seat with meals")
    case _:
        print("Invalid seat type")
