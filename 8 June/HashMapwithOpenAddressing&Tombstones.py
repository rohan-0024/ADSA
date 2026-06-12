# HashMap with Open Addressing and Tombstones
def HASH(key,capacity):
    return (key % 5) % capacity
class HashMap():
    def __init__(self):
        self.capacity = 8
        self.mymap = [-1] * self.capacity
        self.counter = 0
        self.load_fac = self.counter / self.capacity
        
    def put(self, key, value):
        self.counter += 1
        i = index = HASH(key,self.capacity)
        if self.mymap[index] == -1 or self.mymap[index] == -2:
            self.mymap[index] = (key, value)
            print(self.mymap)
            return "Element Added Successfully"
        else:
            probe = 1
            index = (index + probe) % self.capacity
            while index != 1:
                
                if self.mymap[index] == -1 or self.mymap[index] == -2:
                    self.mymap[index] = (key, value)
                    print(self.mymap)
                    index = (index + probe) % self.capacity
                    return "Element Added by probing Successfully "

hm = HashMap()
print(hm.put(2,100))
print(hm.put(7,200))