"""2077. 殊途同归"""


class Solution:
    def numberOfPaths(self, n: int, corridors: list[list[int]]) -> int:
        graph = [set() for _ in range(n + 1)]
        for x, y in corridors:
            graph[x].add(y)
            graph[y].add(x)
        return sum(
            1
            for x in range(1, n + 1)
            for y in graph[x]
            if y > x
            for z in graph[x] & graph[y]
            if z > y
        )


if __name__ == "__main__":
    test_cases = [((5, [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfPaths(*args) == expected
