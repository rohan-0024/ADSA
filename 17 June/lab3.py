# find bfs order and count number of reahable nodes from source

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def reachable(self, source):
        visited = [False] * self.n
        bfs_order = []

        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return bfs_order, len(bfs_order)


data = list(map(int, input().split()))

n = data[0]
m = data[1]

g = Graph(n)

index = 2

for _ in range(m):
    u = data[index]
    v = data[index + 1]
    g.add_edge(u, v)
    index += 2

source = data[index]

order, count = g.reachable(source)

print("BFS Order:", *order)
print("Reachable:", count)
