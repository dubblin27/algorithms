# 5 3 4 1 2 

# 5           3 4 1 2 
# 3 5         4 1 2 
# 3 4 5       1 2 
# 1 3 4 5     2

# 1 2 3 4 5


def insertion_sort(lst):
    for i in range(1,len(lst)):
        key = lst[i] # stores the current element
        j = i-1 
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j-=1 
        lst[j+1] = key 
    return lst
a = [4,2,3,1]
print(insertion_sort(a))