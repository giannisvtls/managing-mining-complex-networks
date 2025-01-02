import time
import networkx as nx

def compactForwards(graph):
    print('Running Compact Forward Algorithm...')
    start_time = time.time()

    # Sort nodes by degree and relabel them
    nodes = sorted(graph.nodes(), key=lambda x: graph.degree(x))
    node_map = {node: i for i, node in enumerate(nodes)}
    graph = nx.relabel_nodes(graph, node_map)

    triangles = 0
    for u in graph.nodes():
        # Get neighbors of u that come after u in the sorted order
        neighbors = [v for v in graph.neighbors(u) if v > u]
        # Count triangles involving the u node
        for i, v in enumerate(neighbors):
            for w in neighbors[i + 1:]:
                if graph.has_edge(v, w):
                    triangles += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return triangles
