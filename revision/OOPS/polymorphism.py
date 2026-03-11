        #POLYMORPHISM
#when the same operator or function behaves differently for different types of data, it is called polymorphism.

#operator overloading
# print(2+3) #5

# print("Hello"+"World") #HelloWorld  
# print([1,2]+[3,4]) #[1, 2, 3, 4] merge


# class complex:
#         def __init__(self,real,imaginary):
#                 self.real=real
#                 self.imaginary=imaginary
        
#         def shownumber(self):
#                 print(f"{self.real}+{self.imaginary}j")

#         def __add__(self,num2):
#                 real=self.real+num2.real
#                 imaginary=self.imaginary+num2.imaginary
#                 return complex(real,imaginary)
#         def __sub__(self,num2):
#                 real = self.real - num2.real
#                 imaginary = self.imaginary - num2.imaginary
#                 return complex(real, imaginary)
              
    
# num1 = complex(2,3)
# num1.shownumber() #2+3j   

# num2 = complex(5, 6)
# num2.shownumber() #5+6j

# num3 = num1 + num2
# num3.shownumber() #7+9j

# num4 = num1 - num2
# num4.shownumber() #-3-3j

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 22/7 * self.radius * self.radius
#     def perimeter(self):
#         return 2 * 22/7 * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self, name, dept, salary):
#         self.name = name
#         self.dept = dept
#         self.salary = salary

#     def show_details(self):
#         print(f"Name: {self.name}, Department: {self.dept}, Salary: {self.salary}")

# # e1 = Employee("Amey", "Dev", 50000)
# # e1.show_details()

# class Engineer(Employee):
#     def __init__(self, name, dept, salary, field):
#         super().__init__(name, dept, salary)
#         self.field = field
#         super().__init__("Engineer", "Development", 60000)

# e2 = Engineer("Amey", "Dev", 50000, "Software")
# e2.show_details()

