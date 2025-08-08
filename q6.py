def find_first_negative(lst):
    """
    - Finds the first negative number in lst using a while loop.
    - Returns the first negative number if found.
    - Returns "No negatives" if none found.
    """
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"

# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)  # Output: -1

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)  # Output: No negatives
