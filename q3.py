def update_dictionary(dct, key, value):
    """
    - Update dictionary dct with key-value pair.
    - If key exists, print the original value before updating.
    - Return the updated dictionary.
    """
    if key in dct:
        print("Original value:", dct[key])
    dct[key] = value
    return dct

# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Expected output: {'name': 'Alice'}

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
# Expected output: Original value: 25
print(result2)  # Expected output: {'age': 26}
