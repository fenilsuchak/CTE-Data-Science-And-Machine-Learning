import numpy as np 
import time
import sys
python_list1 = [i for i in range(10**8)]
python_list2 = [2*i for i in range(10**8)]
print("done")
numpy_array1 = np.arange(0,10**8,1)
numpy_array2 = 2*numpy_array1
added_python_list = []
#Now adding the two python lists
start = time.time()
for i in range(len(python_list1)):
	added_python_list.append(python_list1[i] + python_list2[i])
end = time.time()
print("Time Taken to Add two Python lists:",end-start)

start = time.time()
added_numpy_array = numpy_array1 + numpy_array2
end = time.time()
print("Time Taken to Add two Numpy Arrays:",end-start)
sys.exit()