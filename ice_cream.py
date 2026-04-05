"""
Kevin Nelson
Module 01 Programming Project
 
This program prompts user's for their state and ice cream amount then gives them discounts and addons depending on their state
"""

def CalcPrice(state_string: str, total_amount: float):
    discount = 0
    price_increase = 0

    if state_string == "Arizona":
        discount = 0.1
    elif state_string == "Colorado":
        discount = 0.15
    elif state_string == "Rhode Island":
        price_increase = 5

    return total_amount + (-(total_amount * discount)) + price_increase

total = CalcPrice(input("Enter your state's name: "), float(input("Enter the total of your ice cream purchase: ")))
print(f"Your new price after all regional discounts and increases is: {total}")