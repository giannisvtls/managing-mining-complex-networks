from itertools import combinations
import time


def nodeIterator(graph):
    print('Running Node Iterator Algorithm...')
    start_time = time.time()
    triangles = 0

    # For each node, examine pairs of its neighbors to find triangles
    # to avoid checking all possible node triplets in the graph
    for node in graph.nodes():
        # Get all neighbors of current node for O(1) lookups
        neighbors = list(graph.neighbors(node))

        # Check each pair of neighbors to see if they connect and form a triangle
        # Only check neighbors[i] with neighbors[j] where j>i to avoid duplicates
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if graph.has_edge(neighbors[i], neighbors[j]):
                    triangles += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    # Divide by 3 since each triangle was counted once from each of its vertices
    triangles = int(triangles / 3)

    return triangles