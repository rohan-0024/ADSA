class queuebyStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, data):
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(data)
        print(self.stack1)
        
    def dequeue(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        print(self.stack2)
        

            
    