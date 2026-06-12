# hashset with open Addressing and linear probes

def HASH(key, capacity):
    hash = (key % 5) % capacity
    return  hash


class HashSet():
    def __init__(self):
        self.capacity = 8
        self.array = [-1] * self.capacity
        self.counter = 0
        self.load_fac = self.counter / self.capacity
        
    def add(self, key):
        self.counter += 1
        i = hash = HASH(key,self.capacity)
        if self.array[hash] == -1 or self.array[hash] == -2:
            self.array[hash] = key
            print(self.array)
            return "Added element"
        else:
            probe = 1
            hash = (hash + probe) % self.capacity
            while hash != i:
                hash = (hash + probe) % self.capacity
                if self.array[hash]  == -1 or self.array[hash] == -2:
                    self.array[hash] = key
                    print(self.array)
                    return "Added Element Probe"
                
        print(self.array)
        return "Array Full" 
    def remove(self,key):
        self.counter -= 1
        i = hash = HASH(key,self.capacity)
        if self.array[hash] == key:
            self.array[hash] = -2
            print(self.array)
            return "Deleted Element"
        else:
            probe = 1
            hash = (hash + probe) % self.capacity
            while hash != i:
                hash = (hash + probe) % self.capacity
                if self.array[hash] == key:
                    self.array[hash] = -2
                    print(self.array)
                    return "Deleted Element Probe"
                
        print(self.array)
        return "Array Full" 
    
    def contains(self,key):
        i = hash = HASH(key,self.capacity)
        if self.array[hash] == key:
            return f"{key} is found at index {hash}"
        else:
            probe = 1
            hash = (hash + probe) % self.capacity
            while hash != i:
                hash = (hash + probe) % self.capacity
                if self.array[hash] == key:
                    return f"{key} is found at index {hash}"
                
        print(self.array)
        return "Array Full"  
    
    def resize():
        return
        
        
               
                    
hm= HashSet()
print(hm.add(2))
print(hm.add(3))
print(hm.add(4))
print(hm.add(5))
print(hm.add(6))
print(hm.add(7))
print(hm.add(8))
print(hm.remove(2))
print(hm.remove(7))
print(hm.contains(4))
print(hm.contains(5))

        
        