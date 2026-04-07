#
# @lc app=leetcode.cn id=306 lang=python3
# @lcpr version=30203
#
# [306] 累加数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (first.startswith("0") and len(first) > 1) or (
                    second.startswith("0") and len(second) > 1
                ):
                    continue

                a, b = int(first), int(second)
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c
                if k == n:
                    return True

        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isAdditiveNumber, ("112358",), True),
        (solution.isAdditiveNumber, ("199100199",), True),
        (solution.isAdditiveNumber, ("1023",), False),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
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
# "112358"\n
# @lcpr case=end
