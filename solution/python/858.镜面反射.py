#
# @lc app=leetcode.cn id=858 lang=python3
#
# [858] 镜面反射
#

import os
import sys
from math import gcd


# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common = gcd(p, q)
        horizontal = p // common
        vertical = q // common
        if horizontal % 2 == 0:
            return 2
        return 1 if vertical % 2 else 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mirrorReflection, (2, 1), 2),
        (solution.mirrorReflection, (3, 1), 1),
        (solution.mirrorReflection, (4, 3), 2),
        (solution.mirrorReflection, (3, 2), 0),
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
