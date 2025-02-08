cars = ["ford", "nexus", "volt"]
print(cars[0])
print(len(cars))

for i in cars:
    print(i)

cars.append("Honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("volt")
print(cars)
# Note: The list's remove() method only removes the first occurrence of the specified value.
