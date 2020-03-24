import random as ra
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            count = 0
            arr[i] , arr[i+1] = arr[i+1], arr[i] 
            count = count + 1
    if count != 0 :
        bubble_sort(arr)
    else:
         print(*arr)
   
arr= ra.sample(range(0,100),10)
print(*arr)
bubble_sort(arr)
