#
# @lc app=leetcode.cn id=372 lang=python3
# @lcpr version=30203
#
# [372] 超级次方
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337

        def pow_mod(x: int, n: int) -> int:
            res = 1
            x %= mod
            while n:
                if n & 1:
                    res = res * x % mod
                x = x * x % mod
                n >>= 1
            return res

        if not b:
            return 1
        last = b.pop()
        return pow_mod(self.superPow(a, b), 10) * pow_mod(a, last) % mod
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.superPow, [2, [3]], 8),
        (solution.superPow, [2, [1, 0]], 1024),
        (solution.superPow, [1, [0]], 1),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(args[0], args[1][:])
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# 2\n[3]\n
# @lcpr case=end

#
