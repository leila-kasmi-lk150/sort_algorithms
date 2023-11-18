import random
import timeit

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    else:
        pivot = arr[0]  
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)




array = []
for i in range(10):
    x=random.randint(1,100)
    array.insert(i,x)
print("############################## NOT SORT  ######################################")
print("array not sort :")
print(array)
print("\n")

call = lambda: quick_sort(array)
elapsed_time=timeit.timeit(call, number=1000000)

print("##############################  ######################################")
print("Sorted array: \n", array)

print("############################## Elapsed time  ######################################")
print(f"Elapsed time: {elapsed_time} seconds")