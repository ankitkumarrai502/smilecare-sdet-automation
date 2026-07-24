"""
Reference solutions for day01_exercises.py.
Only look after you've genuinely attempted each TODO yourself.
"""

# 1
product_name = "Ibuprofen 200mg"
price = 12.5
stock_count = 85
print(f"{product_name} costs ${price} and has {stock_count} units in stock")

# 2
quantity = 4
subtotal = price * quantity
print(f"Subtotal: {round(subtotal, 2)}")

# 3
category = input("Enter a category name: ")
if category == "Antibiotics":
    print("Prescription required")
elif category == "Pain Relief":
    print("Over the counter")
else:
    print("Unknown category")

# 4
if stock_count > 0:
    print("In stock")
else:
    print("Out of stock")

# 5
for test_value in [0, 5, 85]:
    if test_value == 0:
        print("Out of stock")
    elif test_value < 10:
        print("Low stock - reorder soon")
    else:
        print("In stock")
