class TriestBase:
    def __init__(self, M):
        self._M = M
        self._sample = EdgeSample()
        self._globalT = 0
        self._localT = {}
        self._t = 0

    def sample_edge(self, u, v):
        # Always allow sampling until the reservoir is full
        return self._t <= self._M

    def update_counters(self, u, v, op):
        # Same as before, but only handle additions
        if op == '+':
            common_neighborhood = self._sample.get_intersection_neighborhood(u, v)
            if not common_neighborhood:
                return

            for c in common_neighborhood:
                self._globalT += 1
                self._localT[c] = self._localT.get(c, 0) + 1
                self._localT[u] = self._localT.get(u, 0) + 1
                self._localT[v] = self._localT.get(v, 0) + 1

    def flip_biased_coin(self):
        # Biased coin is no longer needed since we don't handle deletions
        return True

    def return_counters(self):
        # Scaling factor remains the same
        estimate = max(1, (self._t * (self._t - 1) * (self._t - 2)) /
                          (self._M * (self._M - 1) * (self._M - 2)))
        global_estimate = int(estimate * self._globalT)

        for key in self._localT:
            self._localT[key] = int(self._localT[key] * estimate)

        return {'global': global_estimate, 'local': self._localT}

    def run(self, u, v):
        self._t += 1
        if self.sample_edge(u, v):
            self._sample.add_edge(u, v)
            self.update_counters(u, v, '+')
