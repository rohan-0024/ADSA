# hashmap for payment gateway

        
class PaymentObject():
    def __init__(self,key, value):
        self.key = key
        self.upiID = key[0]
        self.accNo = key[1]
        self.transID = key[2]
        self.ifsc = key[3]
        self. value = value
        self.next = None
        
    def matchObjects(self, key):
        if self.key == key: return True
        else: return False
    
class PaymentGateway():
    def __init__(self):
        self.capacity = 16
        self.array = [None] * self.capacity
        self.counter = 0
        self.loadFactor = self.counter / self.capacity
    
    def hashTransaction(self, payment_item ):
        return
        
    def __loadFactor(self):
        return self.counter / self.capacity
    

    
    def resize(self):
        return
    
    def put(self, key, value):
        self.counter += 1
        index = self.hashTransaction(key)
        newObject = PaymentObject(key, value)
        if self.array[index] == -1:
            self.array[index] = newObject
            return "Added"
        current = self.array[index]
        while current.next is not None:
            current = current.next
        current.next = newObject
        return "Added"
    
    def get(self,key):
        index = self.hashTransaction(key)
        current = self.array[index]
        while current is not None:
            if current.matchObjects(key):
                return current.value
            current = current.next 
        return "Element Not Found"
    def remove(self,key):
        index = self.hashTransaction(key)
        current = self.array[index]
        while current is not None:
            if current.matchObjects(key):
                current.next = current.next.next
                return 'Element deleted'
            current = current.next 
        return "Element Not Found"
    
    def containsKey(self, key):
        index = self.hashTransaction(key)
        current = self.array[index]
        while current is not None:
            if current.matchObjects(key):
                return True
            current = current.next
        return False
                
    
    def size(self):
        return self.counter
    
    def isEmpty(self):
        return self.counter == 0
    
    def clear(self):
        self.array = [None] * self.capacity
        self.counter = 0
        return
    
    