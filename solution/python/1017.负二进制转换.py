#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

import os
import sys


# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n:
            remainder = n & 1
            digits.append(str(remainder))
            n = (n - remainder) // -2
        return "".join(reversed(digits))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.baseNeg2, (2,), "110"),
        (solution.baseNeg2, (3,), "111"),
        (solution.baseNeg2, (4,), "100"),
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
