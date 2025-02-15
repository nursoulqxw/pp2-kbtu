def find_numbers(n):
    num = 0
    while num <= n:
        if not (num % 3 or num % 4):  # Equivalent to checking num % 3 == 0 and num % 4 == 0
            yield num
        num += 1

# Take user input
n = int(input("Enter a number: "))

# Use the generator and print the results
print(*find_numbers(n))
