def reverse_orders(orders):
    """
    Time Complexity: The rfind() operation is linear, and it is called recursively for each order, leading to quadratic time complexity.
    Space Complexity: The recursion stack and substring creation both contribute to linear space usage.
    """
    if " " not in orders: return orders

    last_space_index = orders.rfind(" ")

    return orders[last_space_index + 1:] + "" + reverse_orders(orders[:last_space_index])


print(reverse_orders("Bagel Sandwich Coffee"))