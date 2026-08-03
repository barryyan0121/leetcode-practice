# @lc app=leetcode.cn id=1334 lang=python3

from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        distances = [[10**9] * n for _ in range(n)]
        for node in range(n):
            distances[node][node] = 0
        for left, right, weight in edges:
            distances[left][right] = distances[right][left] = weight
        for middle in range(n):
            for left in range(n):
                for right in range(n):
                    distances[left][right] = min(
                        distances[left][right],
                        distances[left][middle] + distances[middle][right],
                    )
        return min(
            range(n),
            key=lambda node: (
                sum(distance <= distanceThreshold for distance in distances[node]) - 1,
                -node,
            ),
        )


if __name__ == "__main__":
    test_cases = [
        (
            Solution().findTheCity,
            (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4),
            3,
        ),
        (
            Solution().findTheCity,
            (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2),
            0,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1334 题 "阈值距离内邻居最少的城市" 所有测试用例通过')
