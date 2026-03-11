        #POLYMORPHISM
#when the same operator or function behaves differently for different types of data, it is called polymorphism.

#operator overloading
# print(2+3) #5

# print("Hello"+"World") #HelloWorld  
# print([1,2]+[3,4]) #[1, 2, 3, 4] merge


class complex:
        def __init__(self,real,imaginary):
                self.real=real
                self.imaginary=imaginary
        
        def shownumber(self):
                print(f"{self.real}+{self.imaginary}j")

        def __add__(self,num2):
                real=self.real+num2.real
                imaginary=self.imaginary+num2.imaginary
                return complex(real,imaginary)
        def __sub__(self,num2):
                real = self.real - num2.real
                imaginary = self.imaginary - num2.imaginary
                return complex(real, imaginary)
              
    
num1 = complex(2,3)
num1.shownumber() #2+3j   

num2 = complex(5, 6)
num2.shownumber() #5+6j

num3 = num1 + num2
num3.shownumber() #7+9j

num4 = num1 - num2
num4.shownumber() #-3-3j