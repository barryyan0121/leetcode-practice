#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

import os
import sys
from collections import Counter
from functools import reduce
from math import gcd
from typing import List


# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) >= 2


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.hasGroupsSizeX, ([1, 2, 3, 4, 4, 3, 2, 1],), True),
        (solution.hasGroupsSizeX, ([1, 1, 1, 2, 2, 2, 3, 3],), False),
        (solution.hasGroupsSizeX, ([1, 1],), True),
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
