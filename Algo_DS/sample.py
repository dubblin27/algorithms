def ins(arr):
    for i in range(len(arr)):
        key  = arr[i]
        j = i - 1
        while key < arr[j] and j>=0 :
            arr[j+1] = arr[j]
            j-=1 
        arr[j+1] = key
    return arr 
a = [4,2,3,1]
print(ins(a))