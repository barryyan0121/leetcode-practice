# @lc app=leetcode.cn id=1443 lang=python3


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def visit(node: int, parent: int) -> int:
            total = 0
            for child in graph[node]:
                if child != parent:
                    cost = visit(child, node)
                    if cost or hasApple[child]:
                        total += cost + 2
            return total

        return visit(0, -1)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.minTime,
            (
                7,
                [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, True, True, False],
            ),
            8,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1443 题 "收集树上所有苹果的最少时间" 所有测试用例通过')
