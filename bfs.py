from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    paths = {start: [start]}

    while queue:
        current_vertex = queue.popleft()

        if current_vertex not in visited:
            visited.add(current_vertex)

            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    paths[neighbor] = paths[current_vertex] + [neighbor]

    return paths

