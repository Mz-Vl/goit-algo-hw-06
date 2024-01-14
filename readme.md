# Network Analysis for City Transportation Network

## Graph Overview
- **Number of Nodes:** 8
- **Number of Edges:** 13
- **Is Connected:** True

## Degree Centrality
- **Vinnytsia:** 0.29
- **Khmelnytskyi:** 0.57
- **Zhytomyr:** 0.43
- **Rivne:** 0.71
- **Lutsk:** 0.29
- **Lviv:** 0.57
- **Ternopil:** 0.57
- **Ivano-Frankivsk:** 0.29

## Closeness Centrality
- **Vinnytsia:** 0.47
- **Khmelnytskyi:** 0.70
- **Zhytomyr:** 0.58
- **Rivne:** 0.78
- **Lutsk:** 0.54
- **Lviv:** 0.64
- **Ternopil:** 0.70
- **Ivano-Frankivsk:** 0.50

## Betweenness Centrality
- **Vinnytsia:** 0.00
- **Khmelnytskyi:** 0.21
- **Zhytomyr:** 0.06
- **Rivne:** 0.33
- **Lutsk:** 0.00
- **Lviv:** 0.11
- **Ternopil:** 0.19
- **Ivano-Frankivsk:** 0.00

## Analysis Summary

The transportation network of the city exhibits the following characteristics:

1. **Connectivity:** The network is connected, ensuring a continuous transportation flow throughout the city.

2. **Node Distribution:** Nodes exhibit varying degrees of centrality, with Rivne having the highest degree centrality, indicating its significance in the transportation network.

3. **Closeness Centrality:** Rivne also has the highest closeness centrality, suggesting its accessibility to other nodes in the network.

4. **Betweenness Centrality:** Rivne again stands out with the highest betweenness centrality, indicating its crucial role in facilitating communication between other nodes.

The presented analysis provides valuable insights into the structural and functional aspects of the city's transportation network. Further exploration and optimization strategies can be devised based on these centrality metrics.


# Comparison of DFS and BFS Paths in the City Transportation Network

## Results of Algorithm Execution:

### DFS Path:
- `['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Rivne', 'Zhytomyr', 'Lutsk', 'Lviv', 'Ivano-Frankivsk']`

### BFS Paths:
- **Vinnytsia:** `['Vinnytsia']`
- **Khmelnytskyi:** `['Vinnytsia', 'Khmelnytskyi']`
- **Zhytomyr:** `['Vinnytsia', 'Khmelnytskyi', 'Zhytomyr']`
- **Ternopil:** `['Vinnytsia', 'Khmelnytskyi', 'Ternopil']`
- **Rivne:** `['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Rivne']`
- **Ivano-Frankivsk:** `['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Ivano-Frankivsk']`
- **Lviv:** `['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Ivano-Frankivsk', 'Lviv']`
- **Lutsk:** `['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Ivano-Frankivsk', 'Lviv', 'Lutsk']`

## Explanation of Path Differences:

1. **DFS (Depth-First Search):**
   - Starts from 'Vinnytsia' and explores deeper into the graph, choosing the first unvisited neighbor at each vertex.
   - Iterations: `'Vinnytsia' -> 'Khmelnytskyi' -> 'Ternopil' -> 'Rivne' -> 'Zhytomyr' -> 'Lutsk' -> 'Lviv' -> 'Ivano-Frankivsk'`

2. **BFS (Breadth-First Search):**
   - Starts from 'Vinnytsia' and considers all neighbors at the current level before moving on to the next level.
   - Iterations:
      - `'Vinnytsia' -> 'Khmelnytskyi' -> 'Zhytomyr' -> 'Ternopil' -> 'Rivne' -> 'Lutsk' -> 'Lviv' -> 'Ivano-Frankivsk'`
      - `'Vinnytsia' -> 'Khmelnytskyi' -> 'Zhytomyr' -> 'Ternopil' -> 'Rivne' -> 'Lutsk' -> 'Lviv'`

## Conclusion:

- DFS identifies paths that go deeper into the graph, predominantly oriented towards depth.
- BFS considers paths that are distributed at levels and predominantly oriented towards breadth.
  
The difference in paths arises from the distinct approach of these algorithms to graph traversal.
