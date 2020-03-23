#binary Search 

def binary_search(sorted_list,length,key):
    start = 0 
    end = length-1 

    while start <= end :
        mid = (start + end)/2 
        mid = int(mid)
        # print(mid)
        if key == sorted_list[mid]:
            print("found",key,mid)
            break
        elif key < sorted_list[mid]:
            end = mid -1 

        elif key> sorted_list[mid]:
            start = mid+1

lst = list(map(int,input().split()))
n = len(lst)
x = int(input())
lst.sort()
# print(lst,n,x)
binary_search(lst,n,x)

