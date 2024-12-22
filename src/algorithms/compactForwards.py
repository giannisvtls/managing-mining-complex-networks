import time

def compactForwards(graph):
    print('\nRunning Compact Forwards Algorithm...')
    start_time = time.time()
    triangles = 0
    # Order nodes
    nodes = sorted(graph.nodes())  #sort by node ID
    node_index = {node: idx for idx, node in enumerate(nodes)}

    for node in nodes:
        neighbors = [n for n in graph.neighbors(node) if node_index[n] > node_index[node]]
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if graph.has_edge(neighbors[i], neighbors[j]):
                    triangles += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return triangles