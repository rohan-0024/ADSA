# implementing bfs and calculating shortest hop distance

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def bfs(self, edges, source):
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        visited = [False] * self.n
        distance = [-1] * self.n
        bfs_order = []

        q = []

        visited[source] = True
        distance[source] = 0
        q.append(source)

        while len(q) != 0:
            node = q.pop(0)
            bfs_order.append(node)

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    q.append(neighbor)

        return bfs_order, distance


g = Graph(5)
print(g.bfs([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)], 0))
