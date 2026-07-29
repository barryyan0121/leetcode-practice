from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for left, right in pairs:
            root_left, root_right = find(left), find(right)
            if root_left != root_right:
                parent[root_left] = root_right

        groups = defaultdict(list)
        for index, char in enumerate(s):
            groups[find(index)].append(char)
        for chars in groups.values():
            chars.sort(reverse=True)
        return "".join(groups[find(index)].pop() for index in range(len(s)))


if __name__ == "__main__":
    test_cases = [
        ("dcab", [[0, 3], [1, 2]], "bacd"),
        ("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
    ]
    for _, (s, pairs, expected) in enumerate(test_cases):
        assert Solution().smallestStringWithSwaps(s, pairs) == expected
