# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, 
# the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Hazel", "USB cable", 1),
    ("Andrew", "Minecraft", 1),
    ("Katie", "Mic", 2)
    
]

def listOrders(orders):
    for index, order in enumerate(orders, start=1):
        name, product, quantity = order
        print(f"Order {index}:")
        print(f"Customer Name: {name}")
        print(f"Product Ordered: {product}")
        print(f"Quantity: {quantity}")
        print()
listOrders(orders)
