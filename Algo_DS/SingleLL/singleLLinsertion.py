class node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Linked_List:
    def __init__(self):
        self.head = None 

    def append(self,data):
        newnode = node(data)

        if self.head is None :
            self.head = newnode 
            return 
        lastnode = self.head 
        while lastnode.next:
            lastnode = lastnode.next 
        lastnode.next = newnode

    def printll(self):
        currentnode = self.head 
        while currentnode:
            print(currentnode.data)
            currentnode = currentnode.next

    def append_start(self,data):
        newnode = node(data)
        newnode.next = self.head 
        self.head = newnode

    def append_middle(self,dataa,data):
        prev_node = node(dataa)
        xnode = self.head 
        count = 0
        while xnode :
            if prev_node.data == xnode.data :
                prev_node = xnode
                break
            xnode = xnode.next
        if not prev_node:
            print("not in list")
            return 
        newnode = node(data)
        newnode.next = prev_node.next 
        prev_node.next = newnode

#driver_code
ll = Linked_List()
while True : 
    print("\n1.append at end\n2.append at start\n3.append at middle\n4.print")
    option = int(input("enter an option : "))
    if option == 1 :
        data = int(input("enter value to append : "))
        ll.append(data)
    if option == 2 :
        data = int(input("enter value to append : "))
        ll.append_start(data)
    if option == 3 :
        data = int(input("enter current value  : "))
        data1 = int(input("enter value to append  : "))
        ll.append_middle(data,data1)
    if option == 4 :
        ll.printll()


    