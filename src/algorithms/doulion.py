import random
import networkx as nx
#from src.algorithms.triplets import triplets
#from src.algorithms.nodeIterator import nodeIterator
#from src.algorithms.compactForwards import compactForwards

def doulion(graph, p, triangle_count_method):
    print('\nRunning Doulion Algorithm...')
    """
     DOULION algorithm for approximate triangle counting.

    Parameters:
    - graph: networkx.Graph
      our  input graph.
    - p: float
      The probability of keeping an edge during sparsification (0 < p ≤ 1).
    - triangle_count_method: function
      A function that counts triangles in a graph (e.g., all_triplets, node_iterator, compact_forward).

    Returns:
    - Approximate triangle count.
    """
    # Step 1: Sparsify the graph by keeping each edge with probability p.
    sparsified_graph = nx.Graph()
    sparsified_graph.add_nodes_from(graph.nodes())
    for u, v in graph.edges():
        if random.random() <p:
            sparsified_graph.add_edge(u, v)
    # Step 2: Count triangles in the sparsified graph using the specified method
    sparse_triangle_count = triangle_count_method(sparsified_graph)

    # Step 3: Scale the triangle count
    scaling_factor = 1 / (p ** 3)
    approximate_triangles = sparse_triangle_count * scaling_factor

    print("Approximate Triangle Count (DOULION) for", str(triangle_count_method.__name__), ":", approximate_triangles)
    return approximate_triangles
