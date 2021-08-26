class PriorityQueue(dict):    
    def add(self, id, priority):
        self[id] = priority
    
    def pop(self):
        id, priority = max(self.items(), key=lambda x: x[1])
        super().pop(id)
        return id


def dijkstra(graph, start, end):
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    pq = PriorityQueue()
    pq.add(start, 0)
    
    visited = [False] * len(graph)
    while pq:
        vertex = pq.pop()
        visited[vertex] = True
        if vertex == end: return dist[vertex]
        for i, weight in enumerate(graph[vertex]):
            
            if visited[i] or not (weight + 1): continue
            new_dist = dist[vertex] + weight
            if dist[i] > new_dist:
                dist[i] = new_dist
                pq.add(i, new_dist)


with open('input.txt') as file:
    n, s, f = map(int, file.readline().split())
    matrix = tuple(zip(*([map(int, file.read().split())] * n)))

print(dijkstra(matrix, s - 1, f - 1), file=open('output.txt', 'w'))