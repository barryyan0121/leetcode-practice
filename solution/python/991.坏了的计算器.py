#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#

import os
import sys


# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            target = target + 1 if target % 2 else target // 2
            operations += 1
        return operations + startValue - target


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.brokenCalc, (2, 3), 2),
        (solution.brokenCalc, (5, 8), 2),
        (solution.brokenCalc, (3, 10), 3),
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
