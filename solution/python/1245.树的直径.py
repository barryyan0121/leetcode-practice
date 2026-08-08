from collections import defaultdict
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        diameter = 0

        def dfs(node: int, parent: int) -> int:
            nonlocal diameter
            longest = second_longest = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    length = dfs(neighbor, node) + 1
                    if length > longest:
                        longest, second_longest = length, longest
                    elif length > second_longest:
                        second_longest = length
            diameter = max(diameter, longest + second_longest)
            return longest

        dfs(0, -1)
        return diameter


if __name__ == "__main__":
    test_cases = [([[0, 1], [0, 2]], 2)]
    for _, (edges, expected) in enumerate(test_cases):
        assert Solution().treeDiameter(edges) == expected
