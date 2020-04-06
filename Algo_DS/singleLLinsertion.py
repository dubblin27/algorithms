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
    def append_middle(self,prev_node,data):
        prev_node= node(prev_node)
        print ("prev_node.data : ",prev_node.data)
        if not prev_node:
            print("not in list")
            return
        currentnode = self.head 
        while currentnode:
            if currentnode.data == prev_node.data:
                print("currentnode.data : ",currentnode.data)
                currentnode = prev_node
            currentnode = currentnode.next
        
        newnode = node(data)
        print("newnode.data : ",newnode.data)
        newnode.next = prev_node.next 
        prev_node.next = newnode
ll = Linked_List()
ll.append(1)
ll.append(2)
# ll.printll()
ll.append_start(3)
print("head : ",ll.head.data)
ll.append_middle(1,5)
ll.printll()