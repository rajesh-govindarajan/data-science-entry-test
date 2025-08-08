def find_and_replace(lst, find_val, replace_val):
    """
    - Searches for all occurrences of find_val in lst and replaces them with replace_val.
    - lst must be a list.
    - Returns the modified list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    
    return lst

# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  # Expected output: [1, 5, 3, 4, 5, 5]

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)  # Expected output: ['orange', 'banana', 'orange']

