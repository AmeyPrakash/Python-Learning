#You are given a number N, you need to print its multiplication table.
#input = 5
#output = 5 10 15 ........
def multiplicationTable(N):
    for i in range(1, 11):
        print(i * N, end=" ")


#You are given a string s, you need to print its character at even indices (index starts at 0) 
# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea
def stringJumper(s):
    for i in range(0, len(s), 2):
        print(s[i], end="")        

#Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line

def printInDecreasing(x):
    while(x <= 0):
        print(x, end=" ")
        x -= 1