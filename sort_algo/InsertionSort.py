import random
import timeit

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key





array = []
for i in range(10):
    x=random.randint(1,100)
    array.insert(i,x)
print("############################## NOT SORT  ######################################")
print("array not sort :")
print(array)
print("\n")

call = lambda: insertion_sort(array)
elapsed_time=timeit.timeit(call, number=1000000)

print("##############################  ######################################")
print("Sorted array: \n", array)

print("############################## Elapsed time  ######################################")
print(f"Elapsed time: {elapsed_time} seconds")