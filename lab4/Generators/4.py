def squares(a, b):
    while a <= b:
        yield a * a  # Yield the square of the current number
        a += 1

# Example usage:
a, b = map(int, input("Enter two numbers (a b): ").split())

# Test the generator with a for loop
for square in squares(a, b):
    print(square)
