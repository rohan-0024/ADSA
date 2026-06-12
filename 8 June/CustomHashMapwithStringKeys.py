# to create hash map with string keys

def hash(key,capacity):
        hash = 1
        for ch in key:
            hash = (hash * 31 + ord(ch)) % capacity
        return hash

    
    
class HashMap():
    def __init__(self):
        self.capacity = 8
        self.array = [None] * self.capacity
        self.counter = 0
        self.load_factor = self.counter / self.capacity
    
    def __resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for values in self.array:
            for key, value in values:
                index = hash(key,self.capacity)
                if new_array[index] :
                    new_array[index] = new_array[index].append(key, value)
                new_array[index] = [(key, value)]
        self.array = new_array 
        
    def _put(self, key , value):
        self.counter += 1
        index = hash(key,self.capacity)
        if self.array[index]:
            self.array = self.array[index].append((key, value)) 
        self.array[index] = [(key, value)]
        if self.load_factor > 0.75: self.__resize()
        return self.array[index]
    
    def get(self,key):
        index = hash(key,self.capacity)
        if index >= self.capacity or self.array[index] == None:
            return -1
        return self.array[index]
    
    def remove(self,key):
        self.counter -= 1
        index = hash(key,self.capacity)
        if self.array[index] != None:
            self.array[index] = None
            return "Deleted"
        return "Invalid"
        
        return self.array.pop(index)
    
    def rehash(self):
        return
    
hm = HashMap()
print(hm._put("apple", 3))
print(hm._put("banana", 5))
print(hm.get("apple"))
print(hm.get("mango"))
    