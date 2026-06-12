class minStack:
    def __init__(self):
        self.stack = []
        self.min_st = []
        
    def push(self, val):
        self.stack.append(val)
        if len(self.min_st) == 0:
            self.min_st.append(val)
        else:
            self.min_st.append(min(val, self.min_st[-1]))
    
    def pop(self):
        self.stack.pop()
        self.min_st.pop()
        
    def min(self):
        print("MIN =",self.min_st[-1])
    
    def size(self):
        print("SIZE:", len(self.stack))
    
stack = minStack()
stack.push(5)
stack.push(3)
stack.min()
stack.push(7)
stack.min()
stack.pop()
stack.pop()
stack.min()
stack.size()
    