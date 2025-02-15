def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Take user input
n = int(input("Enter a number: "))

# Test the generator with a for loop
for num in countdown(n):
    print(num, end=" ")
