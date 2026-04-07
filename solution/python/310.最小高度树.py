#
# @lc app=leetcode.cn id=310 lang=python3
# @lcpr version=30203
#
# [310] 最小高度树
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(nums: List[int]) -> List[int]:
        return sorted(nums)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findMinHeightTrees, (4, [[1, 0], [1, 2], [1, 3]]), [1]),
        (
            solution.findMinHeightTrees,
            (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]),
            [3, 4],
        ),
        (solution.findMinHeightTrees, (1, []), [0]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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


#
# @lcpr case=start
# 4\n[[1,0],[1,2],[1,3]]\n
# @lcpr case=end
