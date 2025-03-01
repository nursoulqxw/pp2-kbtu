def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
