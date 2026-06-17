#report basic statistics of a graph

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0 for _ in range(n)] for _ in range (n)]
        self.visited = [[-1] * n] * n
        
    def createGraph(self, data_array):
        if len(data_array) == 0: return
        val1 = data_array.pop(0)
        val2 = data_array.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createGraph(data_array)
    
    def getVertices(self):
        print("Vertices:", self.n)
        return
    
    def getEdges(self):
        noOfEdges = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] == 1:
                    noOfEdges += 1
        print("Edges:", noOfEdges // 2)
        return   
    
    def getDegree(self):
        degree_arr = []
        for i in range(self.n):
            degree = 0
            
            for j in range(self.n):
                if self.graph[i][j] == 1:
                    degree += 1
            
            degree_arr.append(degree)
        return degree_arr
    
    def getMaxDegree(self):
        arr = self.getDegree()
        return max(arr)
        
g = Graph(5)
g.createGraph([0, 1, 0, 2, 1, 2, 1, 3, 3, 4])
g.getVertices()
g.getEdges()
print("Vertices:", g.getDegree())
print("Max Degree:", g.getMaxDegree()) 



        
        
        