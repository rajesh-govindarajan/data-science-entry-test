def check_divisibility(num, divisor):
    """
    - Check if num is divisible by divisor.
    - Both must be numeric.
    - Return True if divisible, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")
    
    if divisor == 0:
        return False
    
    return num % divisor == 0

# Scenario 1
result1 = check_divisibility(10, 2)
print(result1)  # Expected output: True

# Scenario 2
result2 = check_divisibility(7, 3)
print(result2)  # Expected output: False
