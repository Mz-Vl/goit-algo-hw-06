import networkx as nx
import matplotlib.pyplot as plt

from dfs import dfs_recursive
from bfs import bfs

# Part 1

cities_list = ['Vinnytsia', 'Khmelnytskyi', 'Zhytomyr', 'Rivne', 'Lutsk', 'Lviv', 'Ternopil', 'Ivano-Frankivsk']

G = nx.Graph()

G.add_nodes_from(cities_list)

G.add_edge('Vinnytsia', 'Khmelnytskyi', weight=119)
G.add_edge('Vinnytsia', 'Zhytomyr', weight=128)
G.add_edge('Zhytomyr', 'Rivne', weight=188)
G.add_edge('Rivne', 'Lutsk', weight=73)
G.add_edge('Rivne', 'Ternopil', weight=155)
G.add_edge('Rivne', 'Lviv', weight=210)
G.add_edge('Lutsk', 'Lviv', weight=151)
G.add_edge('Khmelnytskyi', 'Ternopil', weight=112)
G.add_edge('Khmelnytskyi', 'Zhytomyr', weight=192)
G.add_edge('Khmelnytskyi', 'Rivne', weight=195)
G.add_edge('Ternopil', 'Ivano-Frankivsk', weight=134)
G.add_edge('Ivano-Frankivsk', 'Lviv', weight=132)
G.add_edge('Ternopil', 'Lviv', weight=127)

# Additional Analysis

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
path = nx.shortest_path(G, 'Vinnytsia', 'Lviv')
avg_dist = nx.average_shortest_path_length(G)

print('\nPart 1\n')
print(f'Number of nodes: {num_nodes}')
print(f'Number of edges: {num_edges}')
print(f'Is connected: {is_connected}')
print(f'\nDegree centrality: {degree_centrality}')
print(f'Closeness centrality: {closeness_centrality}')
print(f'Betweenness centrality: {betweenness_centrality}')
print(f'\nShortest path: {path}')
print(f'Average shortest path length: {avg_dist}')

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print('\nPart 1\n')
print(f'Number of nodes: {num_nodes}')
print(f'Number of edges: {num_edges}')
print(f'Is connected: {is_connected}')
print(f'\nDegree centrality: {degree_centrality}')
print(f'Closeness centrality: {closeness_centrality}')
print(f'Betweenness centrality: {betweenness_centrality}')

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)
plt.show()

# Part 1 - end

# Part 2
print('\nPart 2\n')

dfs_path = dfs_recursive(G, 'Vinnytsia')
bfs_paths = bfs(G, 'Vinnytsia')

print(f'DFS path: {dfs_path}')
print(f'BFS path: {bfs_paths}')

# Part 2 - end

# Part 3
print('\nPart 3\n')

shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))

source = 'Vinnytsia'
target = 'Lviv'

shortest_path = shortest_paths[source][target]
shortest_distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')

print(f"Shortest path from {source} to {target}: {shortest_path}")
print(f"Shortest distance: {shortest_distance} km")

# Part 3 - end
