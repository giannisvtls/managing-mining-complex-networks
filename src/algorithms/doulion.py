import random
import networkx as nx
import time

def doulion(graph, p, triangle_count_method):
   start_time = time.time()
   print('\nRunning Doulion Algorithm...')

   # Create sparsified graph by randomly sampling edges with probability p
   # This reduces computation time at the cost of accuracy
   sparsified_graph = nx.Graph()
   sparsified_graph.add_nodes_from(graph.nodes())
   for u, v in graph.edges():
       if random.random() < p:
           sparsified_graph.add_edge(u, v)

   # Count triangles in reduced graph using provided counting method
   # The sparsified graph has fewer edges, so counting is faster
   sparse_triangle_count = triangle_count_method(sparsified_graph)

   # Scale triangle count by 1/p³ to compensate for edge removal
   # Each triangle requires 3 edges, each kept with probability p
   scaling_factor = 1 / (p ** 3)
   approximate_triangles = sparse_triangle_count * scaling_factor
   
#    print("Approximate Triangle Count (DOULION) for", str(triangle_count_method.__name__), ":", approximate_triangles)
   print(f"--- {time.time() - start_time:.4f} seconds ---")
   
   return approximate_triangles