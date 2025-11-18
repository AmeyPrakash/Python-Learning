x = 5 #int(input("Enter a no."))
fact = 1
for i in range(1, 1 + x):
    fact *= i
print(fact)


def fact(n):
    return 1 if (n == 0 or n == 1) else n * fact(n - 1)
y = 5
print(fact(y))



import math as snow
def factorial(s):
    return(snow.factorial(s))
t = 5
print(factorial(t))




import numpy as night
m = 5
left = night.prod([i for i in range(1, m + 1)])
print(left)