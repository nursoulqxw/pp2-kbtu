import math

# Function to convert degrees to radians
def degree_to_radian(deg):
    return deg * (math.pi / 180)

# Take user input
degree = float(input("Input degree: "))

# Convert and print result
print("Output radian:", round(degree_to_radian(degree), 6))
