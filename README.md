# Graph Triangle Counter

A Python implementation of various triangle counting algorithms for graph analysis. This tool provides multiple methods to count or estimate the number of triangles in an undirected graph, including exact counting and probabilistic estimation approaches.

## Algorithms Implemented

- **Triplets**: A basic triangle enumeration algorithm
- **Node Iterator**: An efficient node-centric triangle counting approach
- **Compact Forward**: An optimized version of forward triangle counting
- **TRIEST**: A streaming-based triangle estimation algorithm
- **Doulion**: A probabilistic triangle counting method

## Prerequisites

- Python 3.x
- NetworkX library
- Input graph in edge list format

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install required dependencies:
```bash
pip install networkx
```

## Usage

The program can be configured using environment variables:

```bash
export DATASET_TEXT_FILE_NAME='email-Enron.txt'  # Input graph file
export IS_TRIPLETS_ENABLED='true'                # Enable triplets algorithm
export IS_NODE_ITERATOR_ENABLED='true'           # Enable node iterator algorithm
export IS_COMPACT_FORWARD='true'                 # Enable compact forward algorithm
export IS_TRIEST_ENABLED='true'                 # Enable TRIEST estimation
export IS_DOULION_ENABLED='true'                # Enable Doulion sampling
```

Run the program:
```bash
python main.py
```

## Environment Variables

| Variable | Description | Default Value     |
|----------|-------------|-------------------|
| `DATASET_TEXT_FILE_NAME` | Input graph file name | `email-Enron.txt` |
| `IS_TRIPLETS_ENABLED` | Enable triplets algorithm | `true`            |
| `IS_NODE_ITERATOR_ENABLED` | Enable node iterator algorithm | `true`           |
| `IS_COMPACT_FORWARD` | Enable compact forward algorithm | `true`           |
| `IS_TRIEST_ENABLED` | Enable TRIEST estimation | `true`           |
| `IS_DOULION_ENABLED` | Enable Doulion sampling | `true`           |

## Input Format

The input graph should be provided as a text file in edge list format, where each line contains two integers representing the vertices of an edge:
```
1 2
2 3
3 1
```

## Features

- Supports multiple triangle counting algorithms
- Handles self-loops automatically
- Provides exact counts using NetworkX for comparison
- Includes probabilistic estimation methods (TRIEST and Doulion)
- Configurable through environment variables

## Limitations

- Input graph must be undirected
- Large graphs may require significant memory
- TRIEST algorithm uses fixed memory (M=11000)
- Doulion probability is fixed at 0.4