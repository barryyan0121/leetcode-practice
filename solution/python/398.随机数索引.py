#
# @lc app=leetcode.cn id=398 lang=python3
# @lcpr version=30203
#
# [398] 随机数索引
#

import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    result = i
        return result


# @lc code=end


if __name__ == "__main__":
    random.seed(0)

    # 测试用例 (func, args, result)
    def run_case(nums: List[int], target: int) -> int:
        solution = Solution(nums)
        return solution.pick(target)

    test_cases = [
        (run_case, ([1, 2, 3, 3, 3], 3), {2, 3, 4}),
        (run_case, ([1], 1), {0}),
        (run_case, ([2, 2, 2, 2], 2), {0, 1, 2, 3}),
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
# [1,2,3,3,3]\n3\n
# @lcpr case=end
