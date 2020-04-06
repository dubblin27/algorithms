a = int(input("enter a number : "))
arr = []
while a > 0 :
    rem = a%2 
    arr.append(rem)
    a = a//2
string = ""
while arr != []:
    string += str(arr.pop())
print(string)