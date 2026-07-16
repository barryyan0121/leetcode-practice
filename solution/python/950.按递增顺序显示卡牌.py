#
# @lc app=leetcode.cn id=950 lang=python3
#
# [950] 按递增顺序显示卡牌
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        order = deque()
        for card in sorted(deck, reverse=True):
            if order:
                order.rotate(1)
            order.appendleft(card)
        return list(order)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.deckRevealedIncreasing,
            ([17, 13, 11, 2, 3, 5, 7],),
            [2, 13, 3, 11, 5, 17, 7],
        ),
        (solution.deckRevealedIncreasing, ([1, 1000],), [1, 1000]),
        (solution.deckRevealedIncreasing, ([5],), [5]),
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
