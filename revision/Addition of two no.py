a = 4 
b = 4
sum1 = a + b
print(sum1)

c = int(input("Enter the first no"))
d = int(input("Enter the second no"))
sum2 = float (a) + float (b)
print(sum2)


def sum3():
    e = int(input("Enter the first no."))
    f = int(input("Enter the second no."))
    return  e + f
sum3()

def sum4(g, h):
    return g + h
add = sum4(4, 5)
print(add)


sum5 = lambda a, b: a + b
print(sum5(10, 5))




print(sum([10, 5]))
    