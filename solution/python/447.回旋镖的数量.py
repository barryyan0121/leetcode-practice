#
# @lc app=leetcode.cn id=447 lang=python3
# @lcpr version=30203
#
# [447] 回旋镖的数量
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for x1, y1 in points:
            count = defaultdict(int)
            for x2, y2 in points:
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                count[dist] += 1
            for value in count.values():
                total += value * (value - 1)
        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfBoomerangs, ([[0, 0], [1, 0], [2, 0]],), 2),
        (solution.numberOfBoomerangs, ([[1, 1], [2, 2], [3, 3]],), 2),
        (solution.numberOfBoomerangs, ([[1, 1]],), 0),
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
# [[0,0],[1,0],[2,0]]\n
# @lcpr case=end
