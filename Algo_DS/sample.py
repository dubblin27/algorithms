import random
def quicksort(arr):
    n = len(arr)
    if n <=1 :
        return arr 
    else:
        pivot = arr.pop()
    
    less = []
    great = []
    for i in arr:
        if i > pivot :
            great.append(i)
        else:
            less.append(i)
        
    return quicksort(less) + [pivot] + quicksort(great)

arr = random.sample(range(0,10),10)
print(arr)
print(quicksort(arr))