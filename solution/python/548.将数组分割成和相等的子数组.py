#
# @lc app=leetcode.cn id=548 lang=python3
# @lcpr version=30203
#
# [548] 将数组分割成和相等的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                left = prefix[i] - prefix[0]
                mid = prefix[j] - prefix[i + 1]
                if left == mid:
                    seen.add(left)
            for k in range(j + 2, n - 1):
                mid = prefix[k] - prefix[j + 1]
                right = prefix[n] - prefix[k + 1]
                if mid == right and mid in seen:
                    return True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.splitArray, ([1, 2, 1, 2, 1, 2, 1],), True),
        (solution.splitArray, ([1, 2, 1, 2, 1, 2, 1, 2],), False),
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
# [1,2,1,2,1,2,1]\n
# @lcpr case=end
#
