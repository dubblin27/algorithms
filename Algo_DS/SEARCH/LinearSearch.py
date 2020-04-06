#Linear Search 
n = int(input("enter size of the list: "))
lst = list(map(int,input().split()))
found = False 

x = int(input("enter an element to be searched for  : "))
#1
for i in range(len(lst)):
    if x == lst[i]:
        found = True
        print(x,i)
#2
if x in lst:
    print(x,lst.index(x))