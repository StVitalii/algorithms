def belman_ford(graph, start):
    dist = dict.fromkeys(graph.keys(), float('inf'))
    dist[start] = 0
    for i in range(len(graph) - 1):
        relaxed = True
        for vertex, neighbors in graph.items():
            for key, weight in neighbors:
                new_dist = dist[vertex] + weight
                if dist[vertex] != float('inf') and new_dist < dist[key]:
                    dist[key] = new_dist
                    relaxed = False
        if relaxed: break
    return dist
    

(n, m), *edges = (map(int, line.split()) for line in open('input.txt').readlines())

graph = {}
for v1, v2, weight in edges:
    graph[v1] = graph.get(v1, ()) + ((v2, weight),)

bf = belman_ford(graph, 1)
for i in range(1, n + 1):
    bf.setdefault(i, 30000)

print(*(i[1] for i in bf.items()), file=open('output.txt', 'w'))