# monotonic stack 
class monotonicStack:
    def __init__(self,arr):
        self.array = arr
        self.stack = []
        self.ans = [0] * len(self.array)
        
    def findDays(self):
        
        for i in range(len(self.array)):
            if self.stack == []:
                self.stack.append(i)
                continue
            while self.stack != [] and self.array[i] > self.array[self.stack[-1]]:
                self.ans[self.stack[-1]] = i - self.stack[-1]
                self.stack.pop()
            self.stack.append(i)
            
        print(self.ans)
 
arr = [73,74,75,71,69,72,76,73]       
stack = monotonicStack(arr)
stack.findDays()

    
    
            
                
                
        
            
            

            
        
        
             
        
                
            
            