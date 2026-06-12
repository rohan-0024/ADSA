class createqueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity
            
    def enqueue(self, data):
        if self.head == self.tail and self.size == self.capacity:
            print ("Queue is FULL")
            
        
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1
        print(self.queue)
            
    def dequeue(self):
        if self.head == self.tail and self.size == 0:
            print("Queue is empty")
            
        else:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            print(self.queue)
        
        
queue = createqueue(6)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(7)
queue.enqueue(8)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
        