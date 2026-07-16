#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [number for number in nums if number % 2 == 0] + [
            number for number in nums if number % 2
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sortArrayByParity, ([3, 1, 2, 4],), [2, 4, 3, 1]),
        (solution.sortArrayByParity, ([0],), [0]),
        (solution.sortArrayByParity, ([1, 3],), [1, 3]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
