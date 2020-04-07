class node:
    def __init__(self,data):
        self.data = data  
        self.next = None 

class LL : 
    def __init__(self): 
        self.head = None 
    
    def appendstart(self,data): 
        newnode = node(data)
        newnode.next = self.head 
        self.head = newnode 

    def appendmid(self,data,data1):
        prevnode = node(data)
        newnode = node(data1)
        currnode = self.head 
        count = 0
        while currnode:
            if currnode.data == prevnode.data:
                prevnode = currnode
                count = 1
                break 
            else: 
                count = 0 

            currnode = currnode.next
        if count == 0 :
            print("not in list ")
            return
        newnode.next = prevnode.next 
        prevnode.next = newnode
    
    def appendend(self,data):
        newnode= node(data)
        if self.head == None :
            self.head= newnode 
            return
        lastnode = self.head 
        while lastnode.next :
            lastnode = lastnode.next 
        lastnode.next = newnode 
    def print(self):
        currentnode = self.head 
        while currentnode:
            print(currentnode.data)
            currentnode = currentnode.next

    def deletestart(self):
        currnode = self.head
        self.head = currnode.next 
    
    def deleteend(self):
        currnode = self.head
        while currnode:
            if currnode.next is not None :
                prevnode = currnode 
            currnode = currnode.next
        prevnode.next = None


    def deletemid(self,data) : 
        tofindnode = node(data)
        currnode = self.head
        while currnode:
            tofindnode = node(data)
            if currnode.data == tofindnode.data :
               break
            else : 
                xnode = currnode
            currnode = currnode.next 
        xnode.next = currnode.next 
        currnode.next = None

    def swapnodes(self,data,data1) : 
        if data == data1 :
            return 
        prev1 = None 
        curr1 = self.head
        while curr1 and curr1.data != data :
            prev1 = curr1 
            curr1 = curr1.next 
        prev2 = None 
        curr2 = self.head 
        while curr2 and curr2.data != data1 :
            prev2 = curr2 
            curr2 = curr2.next 
        # print(prev1.data, curr1.data , prev2.data, curr2.data)
        temp1 = curr1 
        temp2 = curr2 
        curr2.next = curr1.next 
        prev1.next = curr2 
        prev2.next = temp1
        temp1.next = temp2.next
        # print(temp.data)



ll = LL()
ll.appendend(1)
ll.appendend(2)
ll.appendend(3)
ll.appendend(10)
ll.appendend(30)
ll.print()

ll.swapnodes(2,10)
ll.print()
