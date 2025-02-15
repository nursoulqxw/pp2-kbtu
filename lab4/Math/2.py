def trapezoid(h,b1,b2):
    return (b1+b2) * h / 2

h = float(input("Height:"))
b1 = float(input("b1:"))
b2 = float(input("b2:"))

print(trapezoid(h,b1,b2))