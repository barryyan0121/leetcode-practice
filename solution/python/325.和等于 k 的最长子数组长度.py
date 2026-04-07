#
# @lc app=leetcode.cn id=325 lang=python3
# @lcpr version=30203
#
# [325] 和等于 k 的最长子数组长度
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        first = {0: -1}
        prefix = 0
        ans = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in first:
                ans = max(ans, i - first[prefix - k])
            if prefix not in first:
                first[prefix] = i
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxSubArrayLen, [[1, -1, 5, -2, 3], 3], 4),
        (solution.maxSubArrayLen, [[-2, -1, 2, 1], 1], 2),
        (solution.maxSubArrayLen, [[1, 2, 3], 6], 3),
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
# [1,-1,5,-2,3]\n3\n
# @lcpr case=end

#
