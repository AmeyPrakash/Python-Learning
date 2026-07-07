def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def avg(num1, num2):
    return (num1 + num2) / 2
print("Select an operation : \n"\
      "1.Addition\n"\
        "2.Subtraction\n"\
            "3.Multiplication\n"\
                "4.Division\n"\
                        "5.Average\n")
choice = int(input("Enter Your Choice (1/2/3/4/5)"))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", sub(num1, num2))    
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))    
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))    
elif choice == 5:
    print("Average of ", num1, "&", num2, "=", avg(num1, num2))
else:
    print("Invalid Input")
