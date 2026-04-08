#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30203
#
# [503] 下一个更大元素 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack: List[int] = []

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.nextGreaterElements, ([1, 2, 1],), [2, -1, 2]),
        (solution.nextGreaterElements, ([1, 2, 3, 4, 3],), [2, 3, 4, -1, 4]),
        (solution.nextGreaterElements, ([5, 4, 3, 2, 1],), [-1, 5, 5, 5, 5]),
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
# [1,2,1]\n
# @lcpr case=end
#
