#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counts = Counter(hand)
        for card in sorted(counts):
            frequency = counts[card]
            if frequency:
                for next_card in range(card, card + groupSize):
                    counts[next_card] -= frequency
                    if counts[next_card] < 0:
                        return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isNStraightHand, ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
        (solution.isNStraightHand, ([1, 2, 3, 4, 5], 4), False),
        (solution.isNStraightHand, ([1, 2, 3, 4], 1), True),
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
