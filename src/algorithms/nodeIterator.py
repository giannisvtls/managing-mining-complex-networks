from itertools import combinations
import time


def nodeIterator(graph):
    print('Running Node Iterator Algorithm...')
    start_time = time.time()
    triangles = 0
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if graph.has_edge(neighbors[i], neighbors[j]):
                    triangles += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    triangles = int(triangles/3)

    return triangles
