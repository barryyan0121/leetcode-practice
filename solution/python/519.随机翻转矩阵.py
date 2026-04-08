#
# @lc app=leetcode.cn id=519 lang=python3
# @lcpr version=30203
#
# [519] 随机翻转矩阵
#

import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.mapping = {}

    def flip(self) -> List[int]:
        idx = random.randrange(self.total)
        self.total -= 1
        actual = self.mapping.get(idx, idx)
        self.mapping[idx] = self.mapping.get(self.total, self.total)
        return [actual // self.n, actual % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.mapping.clear()


# @lc code=end


if __name__ == "__main__":

    def run_case(m: int, n: int) -> bool:
        random.seed(0)
        obj = Solution(m, n)
        seen = set()
        for _ in range(m * n):
            r, c = obj.flip()
            assert 0 <= r < m and 0 <= c < n
            seen.add((r, c))
        assert len(seen) == m * n

        obj.reset()
        seen_after_reset = set()
        for _ in range(m * n):
            r, c = obj.flip()
            assert 0 <= r < m and 0 <= c < n
            seen_after_reset.add((r, c))
        assert len(seen_after_reset) == m * n
        return True

    test_cases = [
        (run_case, (2, 3), True),
        (run_case, (1, 1), True),
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
# 2\n3\n
# @lcpr case=end
#
