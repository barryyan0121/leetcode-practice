#
# @lc app=leetcode.cn id=638 lang=python3
# @lcpr version=30203
#
# [638] 大礼包
#

import sys
import os
from functools import cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        n = len(price)
        special = [
            sp for sp in special if sum(sp[i] * price[i] for i in range(n)) > sp[-1]
        ]

        @cache
        def dfs(state: Tuple[int, ...]) -> int:
            best = sum(state[i] * price[i] for i in range(n))
            for sp in special:
                nxt = tuple(state[i] - sp[i] for i in range(n))
                if min(nxt) >= 0:
                    best = min(best, sp[-1] + dfs(nxt))
            return best

        return dfs(tuple(needs))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shoppingOffers, ([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]), 14),
        (
            solution.shoppingOffers,
            ([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]),
            11,
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
