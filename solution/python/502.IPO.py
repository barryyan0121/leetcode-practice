#
# @lc app=leetcode.cn id=502 lang=python3
# @lcpr version=30203
#
# [502] IPO
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(capital, profits))
        available: List[int] = []
        idx = 0

        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(available, -projects[idx][1])
                idx += 1
            if not available:
                break
            w -= heapq.heappop(available)

        return w


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findMaximizedCapital,
            (2, 0, [1, 2, 3], [0, 1, 1]),
            4,
        ),
        (
            solution.findMaximizedCapital,
            (3, 0, [1, 2, 3], [0, 1, 2]),
            6,
        ),
        (
            solution.findMaximizedCapital,
            (1, 2, [1, 2, 3], [1, 1, 2]),
            5,
        ),
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
# k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]\n
# @lcpr case=end
#
