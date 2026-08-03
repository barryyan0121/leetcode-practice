# @lc app=leetcode.cn id=1557 lang=python3


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        has_incoming = {target for _, target in edges}
        return [vertex for vertex in range(n) if vertex not in has_incoming]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findSmallestSetOfVertices,
            (6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 5]]),
            [0, 3],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1557 题 "可以到达所有点的最少点数目" 所有测试用例通过')
