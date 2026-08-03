# @lc app=leetcode.cn id=1519 lang=python3

from collections import Counter


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        result = [0] * n

        def visit(node: int, parent: int) -> Counter:
            counts = Counter({labels[node]: 1})
            for child in graph[node]:
                if child != parent:
                    counts.update(visit(child, node))
            result[node] = counts[labels[node]]
            return counts

        visit(0, -1)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.countSubTrees,
            (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"),
            [2, 1, 1, 1, 1, 1, 1],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1519 题 "子树中标签相同的节点数" 所有测试用例通过')
