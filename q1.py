# Assuming the swap function is already defined as:

def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x = x + y
    y = x - y
    x = x - y
    print(x, y)

# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
print("Result 1:", result1)  # Expected output: -1

# Scenario 2: 9, 17
result2 = swap(9, 17)
print("Result 2:", result2)  # Expected output: prints "17 9" and then None (because swap prints but returns None)



  
