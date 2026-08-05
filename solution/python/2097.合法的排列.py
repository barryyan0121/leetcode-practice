"""2097. 合法的排列"""


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = {}
        degree = {}
        for start, end in pairs:
            graph.setdefault(start, []).append(end)
            degree[start] = degree.get(start, 0) + 1
            degree[end] = degree.get(end, 0) - 1
        start = next(
            (node for node, value in degree.items() if value == 1), pairs[0][0]
        )
        path = []

        def visit(node):
            while graph.get(node):
                visit(graph[node].pop())
            path.append(node)

        visit(start)
        path.reverse()
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]


if __name__ == "__main__":
    test_cases = [(([[5, 1], [4, 5], [11, 9], [9, 4]],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert len(Solution().validArrangement(*args)) == expected
