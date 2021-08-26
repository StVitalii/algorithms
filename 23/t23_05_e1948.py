def topological_sort(graph, key):
    result = []
    visited = set()

    def _helper(key):
        for neighbor in graph[key]:
            if neighbor not in visited:
                visited.add(neighbor)
                _helper(neighbor)
        result.insert(0, key)
    _helper(key)
    return result


(n, m), *edges = zip(*([map(int, open('input.txt').read().split())] * 2))

dct = {}
for v1, v2 in edges:
    dct[v1] = dct.get(v1, []) + [v2]

print(topological_sort(dct, ))