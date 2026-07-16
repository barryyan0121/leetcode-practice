#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#

import os
import sys


# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n > 4 * len(s):
            return False
        return all(bin(value)[2:] in s for value in range(n // 2 + 1, n + 1))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.queryString, ("0110", 3), True),
        (solution.queryString, ("0110", 4), False),
        (solution.queryString, ("1", 1), True),
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
