#
# @lc app=leetcode.cn id=2685 lang=python3
# @lcpr version=30203
#
# [2685] 统计完全连通分量的数量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False] * n
        ans = 0
        for start in range(n):
            if seen[start]:
                continue

            stack = [start]
            seen[start] = True
            nodes = 0
            degree_sum = 0
            while stack:
                node = stack.pop()
                nodes += 1
                degree_sum += len(graph[node])
                for nxt in graph[node]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        stack.append(nxt)

            if degree_sum == nodes * (nodes - 1):
                ans += 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countCompleteComponents, (6, [[0, 1], [0, 2], [1, 2], [3, 4]]), 3),
        (
            solution.countCompleteComponents,
            (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]),
            1,
        ),
        (solution.countCompleteComponents, (1, []), 1),
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
