class stack:
    def __init__(self):
        self.items  = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def printt(self):
        return self.items

def rev_string(ss,string):
    for i in range(len(string)):
        ss.push(string[i])
    main_str = ""
    while not ss.is_empty():
        main_str += ss.pop()
    return main_str
ss = stack()
x = input("enter a string : ")
print(rev_string(ss,x))
