#positional
def greet(name):
    print(name)

greet("\nAmey")

#keyword

def greet(name, age):
    print("\n",name, age)

greet(age=20, name="Amey")

#default
def greet(name="Guest"):
    print("\n",name)

greet()

#variable length
def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("\n",sum)
add(1, 2, 3, 4, 5)

#kwargs
def details(**info):
    print("\n",info)

details(name="Amey", age=20)

#return
def square(x):
    return x * x
result = square(5)
print("\nSquare of 5 is:", result)

#nested
def outer():
    def inner():
        print("\nThis is the inner function.")
    print("\nThis is the outer function.")
    inner()
outer()

#decorator
def decorator(func):
    def wrapper():
        print("\nBefore")
        func()
        print("\nAfter")
    return wrapper
@decorator
def say_hello():
    print("\nHello!")
say_hello()