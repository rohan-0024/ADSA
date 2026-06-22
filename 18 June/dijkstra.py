import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, source):
        distance = [float("inf")] * self.vertices
        distance[source] = 0

        min_heap = []
        heapq.heappush(min_heap, (0, source))

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_distance > distance[current_node]:
                continue

            for neighbour, weight in self.graph[current_node]:
                new_distance = current_distance + weight

                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbour))

        return distance


g = Graph(4)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)

print(g.dijkstra(0))