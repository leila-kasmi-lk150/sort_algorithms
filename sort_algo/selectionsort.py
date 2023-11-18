import random
import timeit

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
array = []
for i in range(100):
    x=random.randint(1,100)
    array.insert(i,x)
print("############################## NOT SORT  ######################################")
print("array not sort :")
print(array)
print("\n")

call = lambda: selection_sort(array)
elapsed_time=timeit.timeit(call, number=1000000)

print("##############################  ######################################")
print("Sorted array: \n", array)

print("############################## Elapsed time  ######################################")
print(f"Elapsed time: {elapsed_time} seconds")