import time
import networkx as nx
from typing import Callable

def compactForwards(graph):
    print('Running Compact Forward Algorithm...')
    start_time = time.time()

    # Optimize triangle detection by ordering nodes from lowest to highest degree, creating O(1) integer lookups
    degree_map: Callable = lambda x: graph.degree(x)
    nodes = sorted(graph.nodes(), key=degree_map)
    node_map = {node: i for i, node in enumerate(nodes)}
    graph = nx.relabel_nodes(graph, node_map)

    triangles = 0
    for u in graph.nodes():
        # Filter neighbors to only those with higher IDs to avoid counting the same triangle multiple times
        neighbors = [v for v in graph.neighbors(u) if v > u]

        # Iterate through each pair of u's higher-ID neighbors to find triangles
        # Ensures each triangle is counted exactly once
        for i, v in enumerate(neighbors):
            for w in neighbors[i + 1:]:
                if graph.has_edge(v, w):
                    triangles += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return triangles