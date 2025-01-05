import random
import networkx as nx

class triest:

    def __init__(self, M):
        """
        Initialize the Triest-Base algorithm.

        Parameters:
        M (int): The size of the reservoir (sample size).
        """

        self.M = M
        self.S = set()  # Reservoir of edges
        self.t = 0      # Time step
        self.tau = 0    # Total triangle count estimate
        self.tau_c = {} # Count of triangles per node

    def sample_edge(self, edge):
        """
        Decide whether to sample the edge based on the current time step and reservoir size.

        Parameters:
        edge (tuple): The edge (u, v) being considered.

        Returns:
        bool: True if the edge is sampled, False otherwise.
        """
        if self.t <= self.M:
            return True
        elif random.random() < self.M / self.t:
            edge_to_remove = random.choice(list(self.S))
            self.S.remove(edge_to_remove)
            self.update_counters(edge_to_remove, remove=True)
            return True
        return False

    def update_counters(self, edge, remove=False):
        """
        Update the triangle counters after adding or removing an edge.

        Parameters:
        edge (tuple): The edge (u, v) being updated.
        remove (bool): Whether to decrement (True) or increment (False) the counters.
        """
        u, v = edge
        operation = -1 if remove else 1

        # Find the common neighbors of u and v
        neighbors_u = {node for e in self.S for node in e if node != u and u in e}
        neighbors_v = {node for e in self.S for node in e if node != v and v in e}
        common_neighbors = neighbors_u & neighbors_v

        # Update triangle counters
        self.tau += operation * len(common_neighbors)
        for c in common_neighbors:
            self.tau_c[c] = self.tau_c.get(c, 0) + operation

    def process_stream(self, edge_stream):
        """
        Process the edge stream to estimate the number of triangles.

        Parameters:
        edge_stream (iterable): Stream of edges (u, v).
        """
        for edge in edge_stream:
            self.t += 1
            if self.sample_edge(edge):
                self.S.add(edge)
                self.update_counters(edge, remove=False)

    def get_triangle_count(self):
        """
        Get the estimated number of triangles in the graph.

        Returns:
        int: Estimated number of triangles.
        """
        if self.t <= self.M:
            return self.tau
        scaling_factor =(self.t * (self.t - 1) *  (self.t - 2))/ (self.M * (self.M - 1) * (self.M - 2))
        return int(scaling_factor * self.tau)
