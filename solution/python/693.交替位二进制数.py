#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

import os
import sys


# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        value = n ^ (n >> 1)
        return value & (value + 1) == 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.hasAlternatingBits, (5,), True),
        (solution.hasAlternatingBits, (7,), False),
        (solution.hasAlternatingBits, (11,), False),
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
