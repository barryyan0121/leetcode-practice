#
# @lc app=leetcode.cn id=1493 lang=python3
# @lcpr version=30202
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_set = [-1]
        for i, num in enumerate(nums):
            if num == 0:
                zero_set.append(i)
        zero_set.append(len(nums))
        if len(zero_set) == 2 or len(zero_set) == 3:
            return len(nums) - 1
        max_length = 0
        for i in range(1, len(zero_set) - 1):
            start = zero_set[i - 1]
            end = zero_set[i + 1]
            max_length = max(max_length, end - start - 2)
        return max_length
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.longestSubarray, [[1, 0, 0, 0, 0]], 1),
        (solution.longestSubarray, [[1, 1, 0, 1]], 3),
        (solution.longestSubarray, [[0, 1, 1, 1]], 3),
        (solution.longestSubarray, [[1, 1, 1]], 2),
        (solution.longestSubarray, [[0, 0, 0]], 0),
        (solution.longestSubarray, [[1, 0, 1, 0, 1]], 2),
        (solution.longestSubarray, [[0, 1, 1, 1, 0, 1, 1, 0, 1]], 5),
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
# [1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#
