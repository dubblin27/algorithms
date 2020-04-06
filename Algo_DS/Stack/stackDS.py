#stack data structure

class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
s =  Stack()
while True :
    print("1.push\n2.pop\n3.print\n4.check empty\n5.peek")
    x = int(input("enter an option : "))
    
    if x == 1:
        i = int(input("enter an element to push : "))
        s.push(i)
    elif x == 2 :
        s.pop()
    elif x == 3:
        print(s.get_stack())
    elif x==4:
        print(s.is_empty())
    elif x == 5 :
        print(s.peek())
