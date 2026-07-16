#
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#

import os
import sys


# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for digit in s:
            if digit == "1":
                ones += 1
            else:
                flips = min(flips + 1, ones)
        return flips


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minFlipsMonoIncr, ("00110",), 1),
        (solution.minFlipsMonoIncr, ("010110",), 2),
        (solution.minFlipsMonoIncr, ("00011000",), 2),
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
