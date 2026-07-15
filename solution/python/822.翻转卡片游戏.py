#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] 翻转卡片游戏
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned = {front for front, back in zip(fronts, backs) if front == back}
        candidates = (set(fronts) | set(backs)) - banned
        return min(candidates, default=0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.flipgame, ([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]), 2),
        (solution.flipgame, ([1], [1]), 0),
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
