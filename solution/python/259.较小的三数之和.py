#
# @lc app=leetcode.cn id=259 lang=python3
# @lcpr version=30203
#
# [259] 较小的三数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.threeSumSmaller, [[-2, 0, 1, 3], 2], 2),
        (solution.threeSumSmaller, [[0], 0], 0),
        (solution.threeSumSmaller, [[3, 1, 0, -2], 4], 3),
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
# [-2,0,1,3]\n2\n
# @lcpr case=end

#
