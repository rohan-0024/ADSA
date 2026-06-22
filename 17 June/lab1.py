# minimum number of steps to reach from start to target

class Graph:
    def __init__(self, limit):
        self.limit = limit
        self.visited = [-1] * limit
        self.start = 2
        
        self.end = 9
    
    def performOperation(self,x):
        op1 = x + 1
        op2 = x - 1
        op3 = x * 2
        return op1,op2,op3
    
    def inBoundary(self, var):
        return (var > -1 and var < self.limit)
    
    def reachtarget(self):
        if self.start > self.limit: return
        queue= [self.start]
        self.visited[self.start] = 1
        distanceCounter = 0
        while queue:
            for index in range(len(queue)):
                current = queue.pop(0)
                if self.visited[current] != -1:
                    continue
                if current == self.end:
                    return distanceCounter, "Reachable"
                
                var1, var2, var3 = self.performOperation(current)
                if(self.inBoundary(var1)): queue.append(var1)
                if(self.inBoundary(var2)): queue.append(var2)
                if(self.inBoundary(var3)): queue.append(var3)
                self.visited[var1] = 1
                self.visited[var2] = 1
                self.visited[var3] = 1
            
        return "Element not found"
    
g = Graph(10)
print(g.reachtarget())