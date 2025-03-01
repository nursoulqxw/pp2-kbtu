def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

# Example usage
count_case("Hello World!")
