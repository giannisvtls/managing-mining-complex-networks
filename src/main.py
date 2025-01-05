import os
from src.algorithms.triplets import triplets
from src.algorithms.triest import triest
from src.algorithms.nodeIterator import nodeIterator
from src.algorithms.doulion import doulion
from src.algorithms.compactForwards import compactForwards
import networkx as nx

if __name__ == '__main__':
    # String to boolean conversion
    def str_to_bool(env):
        return str(env).lower() in ('true', '1', 't', 'y', 'yes')

    # Read and convert environment variables, defaults to true
    isTripletsEnabled = str_to_bool(os.getenv('IS_TRIPLETS_ENABLED', 'true'))
    isNodeIteratorEnabled = str_to_bool(os.getenv('IS_NODE_ITERATOR_ENABLED', 'true'))
    isCompactForwardEnabled = str_to_bool(os.getenv('IS_COMPACT_FORWARD', 'true'))
    isTriestEnabled = str_to_bool(os.getenv('IS_TRIEST_ENABLED', 'true'))
    isDoulionEnabled = str_to_bool(os.getenv('IS_DOULION_ENABLED', 'true'))

    datasetTextFileName = os.getenv('DATASET_TEXT_FILE_NAME', 'email-Enron.txt')

    def load_dataset(file_name):
        return nx.read_edgelist(file_name, create_using=nx.Graph(), nodetype=int)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{datasetTextFileName}")
    graph = load_dataset(file_path)

    print("\nNumber of selfloops:", nx.number_of_selfloops(graph))
    if nx.number_of_selfloops(graph) > 0:
        graph.remove_edges_from(nx.selfloop_edges(graph))

    triangles_nx = sum(nx.triangles(graph).values()) / 3
    print("\nActual triangles according to networkX:", triangles_nx, "\n")

    if isTripletsEnabled:
        res_triplets = triplets(graph)
        print('Trangle Count (triplets):', res_triplets, '\n')

    if isNodeIteratorEnabled:
        res_nodeiter = nodeIterator(graph)
        print("Triangle Count (node iterator):", res_nodeiter, '\n')

    if isCompactForwardEnabled:
        res_compfw = compactForwards(graph)
        print("Triangle Count (compact forward):", res_compfw, '\n')

    if isDoulionEnabled:
        doulionPropability = 0.4
        if isCompactForwardEnabled:
            doulion(graph, doulionPropability, compactForwards)
        if isNodeIteratorEnabled:
            doulion(graph, doulionPropability, nodeIterator)
        if isTripletsEnabled:
            doulion(graph, doulionPropability, triplets)

    if isTriestEnabled:

        # Triest uses a stream, so we should initialize the stream of the input graph
        edge_stream = list(graph.edges())
        triest_base = triest(M=11000) # initialize the memory we'll use
        triest_base.process_stream(edge_stream)

        estimated_triangles = triest_base.get_triangle_count() #  the estimated number of triangles
        print("\nApproximate triangle count using the TRIEST-base:", estimated_triangles)



