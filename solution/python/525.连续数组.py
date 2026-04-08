#
# @lc app=leetcode.cn id=525 lang=python3
# @lcpr version=30203
#
# [525] 连续数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        ans = 0

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in first_seen:
                ans = max(ans, i - first_seen[balance])
            else:
                first_seen[balance] = i
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findMaxLength, ([0, 1],), 2),
        (solution.findMaxLength, ([0, 1, 0],), 2),
        (solution.findMaxLength, ([0, 0, 1, 0, 0, 0, 1, 1],), 6),
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
# [0,1]\n
# @lcpr case=end
#
