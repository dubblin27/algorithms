# quicksort 
# pivot  = arr[-1]
import random as ra
def quick_sort(arr):
    
    n = len(arr)
    if n <=1:
        return arr 
    else:
        pivot  = arr.pop()
    
    ele_lesser = []
    ele_greater = []

    for item in arr:
        if item > pivot:
            ele_greater.append(item)
        else:
            ele_lesser.append(item)
    return quick_sort(ele_lesser) +[pivot] + quick_sort(ele_greater)

arr= ra.sample(range(0,100),10)
print("before sorting")
print(arr)
print("after sorting")
print(quick_sort(arr))

