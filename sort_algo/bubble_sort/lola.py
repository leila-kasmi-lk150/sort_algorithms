#defenition of bubble sort function
#import numpy as np
#import matplotlib.pyplot as plt
import random
import time
import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#insert 10 values not sort into array, automatically
array1 = []
for i in range(1000):
    x=random.randint(1,100)
    array1.insert(i,x)

print("############################## NOT SORT  ######################################")
print("array not sort :")
print(array1)
print("\n")


#time taken by bubble sort with 10 values
# Define a lambda function to pass parameters to my_function
bubble_sort_call = lambda: bubble_sort(array1)
elapsed_time1=timeit.timeit(bubble_sort_call, number=1000000)
"""start_time = time.time()
bubble_sort(array1)
end_time = time.time()
elapsed_time1 = end_time - start_time"""

print("############################## SORT 10 values ######################################")
print("Sorted array: \n", array1)

print("############################## Elapsed time  ######################################")
print(f"Elapsed time: {elapsed_time1} seconds")


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

#insert 10 values not sort into array, automatically
#array2 = []
#for i in range(100):
 #   x=random.randint(1,100)
  #  array2.insert(i,x)

#print("############################## NOT SORT 10^2 ######################################")
#print("array 2 not sort :")
#print(array2)
#print("\n")


#time taken by bubble sort with 10^2 values
#bubble_sort_call2 = lambda: bubble_sort(array2)
#elapsed_time2=timeit.timeit(bubble_sort_call2, number=1000000)
"""start_time = time.process_time()
bubble_sort(array2)
end_time = time.process_time()
elapsed_time2 = end_time - start_time"""

#print("############################## SORT  ######################################")
#print("Sorted array: \n", array2)

#print("############################## Elapsed time  ######################################")
#print(f"Elapsed time: {elapsed_time2} seconds")



#---------------------------========--------------------------------

#xpoints= np.array([10, 100])
#ypoints= np.array([elapsed_time1, elapsed_time2])
#plt.plot(xpoints, ypoints)
#plt.show()
