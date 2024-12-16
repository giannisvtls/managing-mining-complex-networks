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
    isNodeIteratorEnabled = str_to_bool(os.getenv('IS_NODE_ITERATOR_ENABLED', 'false'))
    isCompactForward = str_to_bool(os.getenv('IS_COMPACT_FORWARD', 'false'))
    isTriestEnabled = str_to_bool(os.getenv('IS_TRIEST_ENABLED', 'false'))
    isDoulionEnabled = str_to_bool(os.getenv('IS_DOULION_ENABLED', 'false'))

    datasetTextFileName = os.getenv('DATASET_TEXT_FILE_NAME', 'email-Enron.txt')
    def load_dataset(file_name):
        return nx.read_edgelist(file_name, create_using=nx.Graph(), nodetype=int)

    dataset = load_dataset(f"{datasetTextFileName}.txt")

    if isTripletsEnabled:
        triplets()

    if isNodeIteratorEnabled:
        nodeIterator()

    if isCompactForward:
        compactForwards()


    if isDoulionEnabled:
        doulion()

    if isTriestEnabled:
        triest()