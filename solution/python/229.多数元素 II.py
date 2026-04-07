#
# @lc app=leetcode.cn id=229 lang=python3
# @lcpr version=30203
#
# [229] 多数元素 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for candidate in [candidate1, candidate2]:
            if candidate is not None and nums.count(candidate) > len(nums) // 3 and candidate not in result:
                result.append(candidate)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(nums: List[int]) -> List[int]:
        return sorted(nums)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.majorityElement, ([3, 2, 3],), [3]),
        (solution.majorityElement, ([1],), [1]),
        (solution.majorityElement, ([1, 2],), [1, 2]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# [3,2,3]\n
# @lcpr case=end
