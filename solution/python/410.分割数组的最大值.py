#
# @lc app=leetcode.cn id=410 lang=python3
# @lcpr version=30203
#
# [410] 分割数组的最大值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can(limit: int) -> bool:
            pieces = 1
            curr = 0
            for num in nums:
                if curr + num > limit:
                    pieces += 1
                    curr = num
                else:
                    curr += num
            return pieces <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.splitArray, [[7, 2, 5, 10, 8], 2], 18),
        (solution.splitArray, [[1, 2, 3, 4, 5], 2], 9),
        (solution.splitArray, [[1, 4, 4], 3], 4),
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
# [7,2,5,10,8]\n2\n
# @lcpr case=end

#
