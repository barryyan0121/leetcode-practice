#
# @lc app=leetcode.cn id=470 lang=python3
# @lcpr version=30203
#
# [470] 用 Rand7() 实现 Rand10()
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
import random
from common.node import *


def rand7() -> int:
    return random.randint(1, 7)


# @lc code=start
class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return 1 + (num - 1) % 10
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    random.seed(0)
    seq = iter([1, 2, 3, 4, 5, 6, 7] * 100)
    globals()["rand7"] = lambda: next(seq)
    test_cases = [
        (solution.rand10, [], range(1, 11)),
        (solution.rand10, [], range(1, 11)),
        (solution.rand10, [], range(1, 11)),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result in expected
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
# \n
# @lcpr case=end

#
