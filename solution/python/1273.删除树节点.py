from collections import defaultdict
from typing import List, Tuple


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = defaultdict(list)
        for node in range(1, nodes):
            children[parent[node]].append(node)

        def dfs(node: int) -> Tuple[int, int]:
            total = value[node]
            count = 1
            for child in children[node]:
                child_total, child_count = dfs(child)
                total += child_total
                count += child_count
            return (total, count) if total else (0, 0)

        return dfs(0)[1]


if __name__ == "__main__":
    test_cases = [(7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1], 2)]
    for _, (nodes, parent, value, expected) in enumerate(test_cases):
        assert Solution().deleteTreeNodes(nodes, parent, value) == expected
