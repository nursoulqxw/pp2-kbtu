# x = lambda a:a+10
# print(x(5))
#output 15

# x = lambda a, b : a * b
# print(x(5,6))
# output = 30

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myFuc(n):
#     return lambda a : a * n

# myTripler = myFuc(3)
# print(myTripler(11))






# def myFunc(n):
#     return lambda a: a * n

# myTripler = myFunc(3)
# myDouble = myFunc(2)

# print(myDouble(11))
# print(myTripler(11))






# def recursion(x):
#     if(x > 0):
#         res = x + recursion(x-1)
#         print(res)
#     else:
#         res = 0
#     return res
# recursion(7)

def myFun(x):
    return lambda a: a * x

mydoubler = myFun(2)
mytripler = myFun(3)

print(mydoubler(11))
print(mytripler(11))