def dfs_recursive(graph, vertex, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(vertex)
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path)
    return path
