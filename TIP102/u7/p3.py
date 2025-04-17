def can_split_coffee(coffee, n):
    """
    Time Complexity: The function explores all possible assignments of coffee batches, leading to exponential time complexity in the worst case.
    Space Complexity: The recursion stack and the current_volumes array contribute to linear space usage relative to m and n.
    """
    # Calculate the total volume of coffee
    total_volume = sum(coffee)
    
    # If the total volume is not divisible by n, return False
    if total_volume % n != 0:
        return False

    # Target volume each person should get
    target = total_volume // n

    # Helper function to check if we can partition the coffee
    def can_partition(index, current_volumes):
        # Base case: if all coffee batches are used, check if all volumes match the target
        if index == len(coffee):
            return all(volume == target for volume in current_volumes)

        # Try adding the current coffee batch to each person's share
        for i in range(n):
            if current_volumes[i] + coffee[index] <= target:
                current_volumes[i] += coffee[index]
                if can_partition(index + 1, current_volumes):
                    return True
                current_volumes[i] -= coffee[index]

            # Optimization: If the current volume is 0, no need to try other empty slots
            if current_volumes[i] == 0:
                break

        return False

    # Initialize the current volumes for each person
    return can_partition(0, [0] * n)

# Example usage
print(can_split_coffee([4, 4, 8], 2))  # Output: True
print(can_split_coffee([5, 10, 15], 4))  # Output: False