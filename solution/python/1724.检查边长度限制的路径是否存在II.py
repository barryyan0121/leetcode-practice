class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: list[list[int]]):
        self.parent = list(range(n))
        self.size = [1] * n
        self.cost = [0] * n
        for left, right, distance in sorted(edgeList, key=lambda edge: edge[2]):
            root_left = self._find(left, distance + 1)
            root_right = self._find(right, distance + 1)
            if root_left == root_right:
                continue
            if self.size[root_left] > self.size[root_right]:
                root_left, root_right = root_right, root_left
            self.parent[root_left] = root_right
            self.cost[root_left] = distance
            self.size[root_right] += self.size[root_left]

    def _find(self, node: int, limit: int) -> int:
        while self.parent[node] != node and self.cost[node] < limit:
            node = self.parent[node]
        return node

    def query(self, p: int, q: int, limit: int) -> bool:
        return self._find(p, limit) == self._find(q, limit)


if __name__ == "__main__":
    test_cases = [
        (
            (6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]),
            [(2, 3, 2), (1, 3, 3), (2, 0, 3), (0, 5, 6)],
            [True, False, True, False],
        )
    ]
    for index, (args, queries, expected) in enumerate(test_cases):
        graph = DistanceLimitedPathsExist(*args)
        assert [graph.query(*query) for query in queries] == expected, index
