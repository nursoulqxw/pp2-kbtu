def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)  # Convert to string for joining later

# Take user input
n = int(input("Enter a number: "))

# Use the generator and print the result
print(",".join(even_generator(n)))
