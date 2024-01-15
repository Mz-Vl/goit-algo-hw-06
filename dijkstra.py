def dijkstra(graph, start, end):
    weights = {node: float('infinity') for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    weights[start] = 0

    unvisited_nodes = set(graph.nodes)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: weights[node])

        for neighbor in graph.neighbors(current_node):
            new_weight = weights[current_node] + graph.get_edge_data(current_node, neighbor).get('weight', 1)
            if new_weight < weights[neighbor]:
                weights[neighbor] = new_weight
                predecessors[neighbor] = current_node

        unvisited_nodes.remove(current_node)

    shortest_path = [end]
    current_node = end
    while current_node != start:
        current_node = predecessors[current_node]
        shortest_path.insert(0, current_node)

    return shortest_path, weights[end]
