# slow/fast split using circular linked list

class node:
    def __init__(self, label):
        self.label = label
        self.next = None
    
def appendNode(head,label):
    while head.next is not None:
        print(head.label,"->")
        head = head.next
    head.next = node(label)
    print(head.next.label)

head = node("A")
appendNode(head,"B")
appendNode(head,"C")


            
        