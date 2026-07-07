#
# @lc app=leetcode.cn id=659 lang=python3
# @lcpr version=30203
#
# [659] 分割数组为连续子序列
#

import sys
import os
from collections import Counter, defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end = defaultdict(int)
        for num in nums:
            if left[num] == 0:
                continue
            left[num] -= 1
            if end[num - 1]:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isPossible, ([1, 2, 3, 3, 4, 5],), True),
        (solution.isPossible, ([1, 2, 3, 3, 4, 4, 5, 5],), True),
        (solution.isPossible, ([1, 2, 3, 4, 4, 5],), False),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

