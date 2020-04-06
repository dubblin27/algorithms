#Balancing paranthesis using stack 
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

class para:
    def __init__(self):
        self.items = []
        self.lisst = []
    def store(self,item):
        self.items.append(item)
        print("your list : ",*self.items)
    def pop(self):
        self.lisst.pop()
    def clear(self):
        self.items = []
    def check(self):
        print("your list : ",*self.items)
        for i in self.items:
            # print(i)
            if i == '{' or i == '(' or i == '['  :
                # print("i : ",i)
                self.lisst.append(i)
                # print(self.lisst)
            if i == '}' : 
                # print(i)
                
                if self.lisst[-1] == '{' : 
                    # print(self.lisst)
                    self.lisst.pop()
            if i == ']' :
                # print(i) 
                if self.lisst[-1] == '[' : 
                    self.lisst.pop()
            if i == ')' : 
                # print(i)
                if self.lisst[-1] == '(' : 
                    self.lisst.pop()
            # print(self.lisst)
            print("self.lisst : ", *self.lisst)
        if self.lisst == []:
            return True
        else:
            return False
        
ss = para()

while True :
    print("1.insert\n2.check balance\n3.clear")
    option = int(input("Enter an option : "))
    if option == 1 :
        im = input("Enter to check if balanced : ")
        ss.store(im)
    if option ==2 :
        print(ss.check())
    if option ==3 :
        ss.clear()
        
