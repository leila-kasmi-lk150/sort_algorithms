import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half) 

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1









array = []
for i in range(10000):
    x=random.randint(1,100)
    array.insert(i,x)
print("############################## NOT SORT  ######################################")
print("array not sort :")
print(array)
print("\n")

call = lambda: merge_sort(array)
elapsed_time=timeit.timeit(call, number=1000000)

print("##############################  ######################################")
print("Sorted array: \n", array)

print("############################## Elapsed time  ######################################")
print(f"Elapsed time: {elapsed_time} seconds")