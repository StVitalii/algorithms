def _dfs_helper(graph, visited, start, end):
    visited.add(start)
    if start == end:
        dfs.solutions.append(visited)
        return
    neighbors = graph.get(start)
    if neighbors:
        for neighbor in neighbors:
            if neighbor not in visited:
                _dfs_helper(graph, visited.copy(), neighbor, end)


def dfs(graph, start, end):
    visited = set()
    dfs.solutions = []
    _dfs_helper(graph, visited, start, end)
    return dfs.solutions
     


(n, k, a, b, d), *arches = (line.split() for line in open('input.txt').readlines())

n, k, d = map(int, (n, k, d))

dct = {}
for v1, v2 in arches:
    dct[v1] = dct.get(v1, []) + [v2]


print(len(list(filter(lambda x: len(x) < d + 2, dfs(dct, '2', '5')))), file=open('output.txt', 'w'))
   