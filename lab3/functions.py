# def my_function():
#     print("hello mf")

# my_function()

# def my_function(fname):
#     print(fname + " Aliyev")

# my_function("Nurislam")
# my_function("Askar")
# my_function("Arystan")

# def my_function(fname, lname):
#     print(fname + " " + lname)

# my_function("Nurislam", "Aliyev")

# def my_function(child3,child2,child1):
#     print("The youngest child is " + child3)
# my_function(child1="Rick", child2="Vic", child3="Nick")

# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname="Nick", lname="Maguire")


# def my_function(country = "Norway"):
#     print("I am from " + country)
# my_function("Sweden")
# my_function()
# my_function("Kazakhstan")
# my_function("Estonia")

# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my_func(x):
#     print(5*x)

# print(my_func(3))
# print(my_func(5))
# print(my_func(10))

# def my_function(x, /):
#   print(x)

# my_function(3)

# def my_func(x):
#     print(x)
# my_func(3)


# def my_func(*, x):
#     print(x)
# my_func(x=3)

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)

#recursion

# def recursion(k):
#     if(k>0):
#         result = k + recursion(k-1)
#         print(result)
#     else:
#         result = 0;
#     return result

# print("Recustion example res:")
# recursion(6)

# recursion(6) → 6 + recursion(5)
# recursion(5) → 5 + recursion(4)
# recursion(4) → 4 + recursion(3)
# recursion(3) → 3 + recursion(2)
# recursion(2) → 2 + recursion(1)
# recursion(1) → 1 + recursion(0)
# recursion(0) → 0  (базовый случай)

# recursion(1) → 1 + 0 = 1
# recursion(2) → 2 + 1 = 3
# recursion(3) → 3 + 3 = 6
# recursion(4) → 4 + 6 = 10
# recursion(5) → 5 + 10 = 15
# recursion(6) → 6 + 15 = 21

def rec_ex(k):
    if(k > 0):
        rez = k + rec_ex(k-1)
        print(rez)
    else:
        rez=0
    return rez
rec_ex(7)