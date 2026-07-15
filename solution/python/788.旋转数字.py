#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

import os
import sys


# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = set("0125689")
        changed = set("2569")
        return sum(
            set(str(number)) <= valid and bool(set(str(number)) & changed)
            for number in range(1, n + 1)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.rotatedDigits, (10,), 4),
        (solution.rotatedDigits, (1,), 0),
        (solution.rotatedDigits, (2,), 1),
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
