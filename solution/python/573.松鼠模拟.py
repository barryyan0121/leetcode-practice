#
# @lc app=leetcode.cn id=573 lang=python3
# @lcpr version=30203
#
# [573] 松鼠模拟
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def dist(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        total = 0
        best_gain = -(10**9)
        for nut in nuts:
            tree_dist = dist(tree, nut)
            total += 2 * tree_dist
            best_gain = max(best_gain, tree_dist - dist(squirrel, nut))
        return total - best_gain


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.minDistance,
            (
                5,
                7,
                [2, 2],
                [4, 4],
                [[3, 0], [2, 5]],
            ),
            12,
        ),
        (
            solution.minDistance,
            (
                3,
                3,
                [1, 1],
                [0, 0],
                [[2, 2]],
            ),
            6,
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


#
# @lcpr case=start
# height = Grid height, width = Grid width\n
# @lcpr case=end
