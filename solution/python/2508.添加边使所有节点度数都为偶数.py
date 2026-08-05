"""2508. 添加边使所有节点度数都为偶数"""


class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        neighbors = [set() for _ in range(n + 1)]
        for first, second in edges:
            neighbors[first].add(second)
            neighbors[second].add(first)
        odd = [node for node in range(1, n + 1) if len(neighbors[node]) % 2]
        if not odd:
            return True
        if len(odd) == 2:
            first, second = odd
            return second not in neighbors[first] or any(
                node not in neighbors[first] and node not in neighbors[second]
                for node in range(1, n + 1)
                if node not in (first, second)
            )
        if len(odd) == 4:
            a, b, c, d = odd
            return (
                (b not in neighbors[a] and d not in neighbors[c])
                or (c not in neighbors[a] and d not in neighbors[b])
                or (d not in neighbors[a] and c not in neighbors[b])
            )
        return False


if __name__ == "__main__":
    test_cases = [((5, [[1, 2], [2, 3], [3, 4], [4, 2]]), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isPossible(*args) == expected
