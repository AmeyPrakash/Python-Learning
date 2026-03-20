import numpy as np
#ZERO ARRAYS

arr_zero = np.zeros(4)
arr1_zero=np.zeros((3,4))
print(arr_zero)
print("\n",arr1_zero)

#ONES

arr_one=np.ones(5)
arr1_one=np.ones((3,4))
print("\n",arr1_one)

print("\n",arr_one)

#EMPTY
arr_empty=np.empty(5)
arr1_empty=np.empty((3,4))
print("\n",arr1_empty)

print("\n",arr_empty)

#RANGE

arr_range=np.arange(5)

print("\n",arr_range)

#diagonal 1s
arr_diagonal=np.eye(3) #where 3 is the dimension
print("\n",arr_diagonal)
arr_diagonal1=np.eye(3,5)
print("\n",arr_diagonal1)
#array with interval
arr_space=np.linspace(1,10,num=5)
print("\n",arr_space)