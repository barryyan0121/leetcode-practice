#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

import os
import sys
from math import gcd


# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        common_multiple = a // gcd(a, b) * b
        left, right = 1, n * min(a, b)
        while left < right:
            middle = (left + right) // 2
            count = middle // a + middle // b - middle // common_multiple
            if count >= n:
                right = middle
            else:
                left = middle + 1
        return left % (10**9 + 7)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.nthMagicalNumber, (1, 2, 3), 2),
        (solution.nthMagicalNumber, (4, 2, 3), 6),
        (solution.nthMagicalNumber, (5, 2, 4), 10),
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
