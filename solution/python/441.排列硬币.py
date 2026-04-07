#
# @lc app=leetcode.cn id=441 lang=python3
# @lcpr version=30203
#
# [441] 排列硬币
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            need = mid * (mid + 1) // 2
            if need <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.arrangeCoins, (5,), 2),
        (solution.arrangeCoins, (8,), 3),
        (solution.arrangeCoins, (1,), 1),
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


#
# @lcpr case=start
# 5\n
# @lcpr case=end
