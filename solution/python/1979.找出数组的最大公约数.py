#
# @lc app=leetcode.cn id=1979 lang=python3
#
# [1979] 找出数组的最大公约数
#

import os
import sys
from math import gcd


# @lc code=start
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return gcd(min(nums), max(nums))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findGCD, ([2, 5, 6, 9, 10],), 2),
        (solution.findGCD, ([7, 5, 6, 8, 3],), 1),
        (solution.findGCD, ([3, 3],), 3),
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
