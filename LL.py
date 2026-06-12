class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertatBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    def insertatEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.inseratBegin(data)
            return 
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def display(self):
        current = self.head
        while current != None:
            print(current.data, "->")
            current = current.next
    
LL = LinkedList()
LL.insertatBegin(10)
LL.insertatBegin(20)
LL.display()
        
        
        


        
        
        
        