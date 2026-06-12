# monotonic dequeue for demand spike
class montonicDeque:
    def __init__(self,array,k):
        self.size= len(array)
        self.k = k
        self.array = array
        self.dequeue = []
        self.values = []
        
    def findWindowMax(self):
        for index in range(len(self.array)):
            if len(self.dequeue) == 0:
                self.dequeue.append(index)
            else:
                if self.dequeue(index)
                
        