#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        incoming = [0] * (n + 1)
        first = second = None

        for a, b in edges:
            if incoming[b]:
                first = [incoming[b], b]
                second = [a, b]
                break
            incoming[b] = a

        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for edge in edges:
            if edge == second:
                continue
            a, b = edge
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return first if first else edge
            parent[root_b] = root_a

        return second


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findRedundantDirectedConnection,
            ([[1, 2], [1, 3], [2, 3]],),
            [2, 3],
        ),
        (
            solution.findRedundantDirectedConnection,
            ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],),
            [4, 1],
        ),
        (
            solution.findRedundantDirectedConnection,
            ([[2, 1], [3, 1], [4, 2], [1, 4]],),
            [2, 1],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)
