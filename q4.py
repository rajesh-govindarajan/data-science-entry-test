def string_reverse(s):
    """
    - Reverses the given string s.
    - s must be a string.
    - Returns the reversed string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s[::-1]
# Scenario 1
result1 = string_reverse("Hello World")
print(result1)  # Output: "dlroW olleH"

# Scenario 2
result2 = string_reverse("Python")
print(result2)  # Output: "nohtyP"
