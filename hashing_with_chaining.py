# hashing with chaining using linked list 

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self. capacity = capacity
        self.array = [None] * self.capacity
        self.count = 0
        
    def hash_func(self,key):
        if isinstance(key, str):
            hash = 0
            for char in key:
                hash += ord(char)
            return hash % self.capacity
        else:
            return key % self.capacity
    
    def insert(self, key, value):
        index = self.hash_func(key)
        new_node = Node(key, value)
        
        if self.array[index] == None:
            self.array[index] = new_node
            self.count += 1
            print(f"  Inserted ({key} : {value}) at index {index}  [No collision]")
            
        else:
            temp = self.array[index]
            
            while temp:
                if temp.key == key:
                    temp.value = value
                    print(f"  Updated ({key} : {value}) at index {index}")
                    return
                if temp.next is None:
                    break
                temp = temp.next
            
            temp.next = new_node
            self.count += 1
            print(f"  Inserted ({key} : {value}) at index {index}  [Collision! Added to chain]")
            
    def search(self, key):
        index = self.hash_func(key)
        temp = self.array[index]
        
        while temp:
            if temp.key == key:
                print("key Found. Value is ", temp.value)
                return
            temp = temp.next
        
        print("Key not Found")
        return None
    
    
    def delete(self,key):
        index = self.hash_func(key)
        temp = self.array[index]
        prev = None
        
        while temp:
            if temp.key == key:
                
                if prev is None:
                    self.array[index] = temp.next
                else:
                    prev.next = temp.next
                    
                self.count -= 1
                print(f"  Deleted key '{key}' from index {index}")
                return True
            prev = temp
            temp = temp.next
        
        print(f"  Key '{key}' not found. Nothing deleted.")
        return False
    
    def display(self):
        for i in range(self.capacity):
            print(f"Bucket [{i}] : ", end = "")
            
            if self.array[i] is None:
                print("Empty")
            else:
                temp = self.array[i]
                chain = []
                while temp:
                    chain.append(f"({temp.key} : {temp.value})")
                    temp = temp.next
                print("-->".join(chain))
        
        print()
        print(f"Total Elements : {self.count}")
        print(f"  Load Factor    : {self.count}/{self.capacity} = {self.count/self.capacity:.2f}")
        print()   

ht = HashTable(7)
ht.insert("AB", 10)
ht.insert("BC", 20)
ht.insert("AB", 100)
ht.insert("BA", 1000 )
ht.search("BC")


ht.display()     
                
        
        