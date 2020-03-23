# 3 6 2 1 4 5

# 1           6 2 3 4 5
# 1 2         6 3 4 5
# 1 2 3       6 4 5
# 1 2 3 4     6 5
# 1 2 3 4 5   6

# 1 2 3 4 5 6 

def sel_sort(a):
    for i in range(len(a)):
        x = min(a[i:])
        ind = a.index(x)
        a[i],a[ind] = a[ind],a[i]
    return a

arr = [3, 6, 2, 1, 4, 5]
print(sel_sort(arr))