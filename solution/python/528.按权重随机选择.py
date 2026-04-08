#
# @lc app=leetcode.cn id=528 lang=python3
# @lcpr version=30203
#
# [528] 按权重随机选择
#

import sys
import os
import random
from bisect import bisect_left

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        return bisect_left(self.prefix, target)


# @lc code=end


if __name__ == "__main__":

    def run_case(weights: List[int], sample_count: int = 20) -> bool:
        random.seed(0)
        obj = Solution(weights)
        picks = [obj.pickIndex() for _ in range(sample_count)]
        assert all(0 <= idx < len(weights) for idx in picks)
        return True

    test_cases = [
        (run_case, ([1, 3],), True),
        (run_case, ([2, 5, 3],), True),
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
# [1,3]\n
# @lcpr case=end
#
