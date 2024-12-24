import os
from src.algorithms.triplets import triplets
from src.algorithms.triest import triest
from src.algorithms.nodeIterator import nodeIterator
from src.algorithms.doulion import doulion
from src.algorithms.compactForwards import compactForwards
import networkx as nx

def print_hi():
    print("""___________ ________  ________ 
\\_   _____//  _____/ /  _____/ 
 |    __)_/   \\  ___/   \\  ___ 
 |        \\    \\_\\  \\    \\_\\  \\
/_______  /\\______  /\\______  /
        \\/        \\/        \\/""")


if __name__ == '__main__':
    print_hi()

    # Helper function for string to boolean conversion
    def str_to_bool(env):
        return str(env).lower() in ('true', '1', 't', 'y', 'yes')

    # Read and convert environment variables
    isTripletsEnabled = str_to_bool(os.getenv('IS_TRIPLETS_ENABLED', 'false'))
    isNodeIteratorEnabled = str_to_bool(os.getenv('IS_NODE_ITERATOR_ENABLED', 'true'))
    isCompactForward = str_to_bool(os.getenv('IS_COMPACT_FORWARD', 'true'))
    isTriestEnabled = str_to_bool(os.getenv('IS_TRIEST_ENABLED', 'false'))
    isDoulionEnabled = str_to_bool(os.getenv('IS_DOULION_ENABLED', 'true'))

    datasetTextFileName = os.getenv('DATASET_TEXT_FILE_NAME', 'email-Enron.txt')
    def load_dataset(file_name):
        return nx.read_edgelist(file_name, create_using=nx.Graph(), nodetype=int)


    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{datasetTextFileName}")
    dataset = load_dataset(file_path)
    graph = dataset # better name?
    p = 0.5  # Probability of keeping an edge for the Doulion algorithm

    if isTripletsEnabled:
        triplets(graph)

    if isNodeIteratorEnabled:
        nodeIterator(graph)

    if isCompactForward:
        compactForwards(graph)

    if isDoulionEnabled:
        doulion(graph, p, nodeIterator)  # Use node_iterator as the exact method

    if isTriestEnabled:
        triest()