"""
file handles control flows and functions in python
"""

def calculate_discount(price, discount_percent):
    if discount_percent <20:
        print("Discount is less than 20%")
        return price
    discount = (price * discount_percent)/100
    final_price = price - discount
    return final_price

def discount_prompter():
    try:
        price = float(input("Enter Original price of item: "))
        discount_percent = float(input("Enter discount on the item in Percentage(%): "))
        final_price = calculate_discount(price, discount_percent)

        if price != final_price:
            print(f"Final price of {price} and discount percentage {discount_percent}% is {final_price:.2f}")
        # print("Discount is less than 20%")
        print(f"Price remains: {final_price:.2f}")
    except ValueError:
        print("Value is not numeric for both discount percentage and Original price")