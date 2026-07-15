#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

import os
import sys
from typing import *

# @lc code=start
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.limit = n - len(blacklist)
        blocked = set(blacklist)
        available = iter(set(range(self.limit, n)) - blocked)
        self.mapping = {
            number: next(available) for number in blacklist if number < self.limit
        }

    def pick(self) -> int:
        number = random.randrange(self.limit)
        return self.mapping.get(number, number)


# @lc code=end


if __name__ == "__main__":
    solution = Solution(7, [2, 3, 5])
    test_cases = [(solution.pick, (), {0, 1, 4, 6}) for _ in range(100)]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result in expected
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
