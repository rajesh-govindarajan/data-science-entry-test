def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x = x + y
    y = x - y
    x = x - y
    print(x, y)

# Scenario 1: "Apple", 10
Output1 = swap("Apple", 10)
print(Output1)  # Expected output: -1

# Scenario 2: 9, 17
Output2 = swap(9, 17)
print(Output2)  # Expected output: prints "17 9" and then None (because swap prints but returns None)
