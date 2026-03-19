#list can store int, string as it accepts every data type
#numpy can merge string and int but should be used with single data type
#list doesn't need installation of any package 
#array needs the package to be installed 
#less efficiency in list for numerical operations
#%timeit gives time of  single code of line
#%%timeit give time of the program
import numpy as np
import time

start = time.time()
[j**4 for j in range(1,9)]
end = time.time()

print("Time:", end - start)


arr = np.arange(1, 10000)

start = time.time()
arr**4
end = time.time()

print(end - start)