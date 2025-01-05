from itertools import combinations
import time


def triplets(graph):
    print('Running Optimized Triplets Algorithm...')
    start_time = time.time()
    triangles = 0

    # Create hash tables of node neighbors to enable O(1) edge lookups instead of O(E) searches
    adj = {node: set(graph.neighbors(node)) for node in graph.nodes()}

    # Only iterate over nodes that have edges
    nodes = [n for n in graph.nodes() if adj[n]]

    # For each edge (u,v), only check nodes w that are neighbors of u
    for u in nodes:
        # Get neighbors with higher node IDs to avoid counting the same triangle multiple times
        u_neighbors = {v for v in adj[u] if v > u}

        for v in u_neighbors:
            # Only check nodes w that are neighbors of u and have higher IDs than v
            w_candidates = {w for w in adj[u] if w > v}
            # Count triangles where w is also connected to v
            triangles += sum(1 for w in w_candidates if w in adj[v])

    print(f"--- {time.time() - start_time:.4f} seconds ---")
    return triangles