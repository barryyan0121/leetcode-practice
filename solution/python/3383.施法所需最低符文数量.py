class Solution:
    def minRunes(self, n: int, crystals: list[int], flowFrom: list[int], flowTo: list[int]) -> int:
        parent = list(range(n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for source, target in zip(flowFrom, flowTo):
            parent[find(source)] = find(target)
        powered = {find(node) for node in crystals}
        return sum(root not in powered for root in {find(node) for node in range(n)})


if __name__ == "__main__":
    test_cases = [
        ((6, [0], [0, 1, 2, 3], [1, 2, 3, 0]), 2),
        ((7, [3, 5], [0, 1, 2, 3, 5], [1, 2, 0, 4, 6]), 1),
    ]
    for _, ((n, crystals, flow_from, flow_to), expected) in enumerate(test_cases):
        assert Solution().minRunes(n, crystals, flow_from, flow_to) == expected
