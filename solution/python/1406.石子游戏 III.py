#
# @lc app=leetcode.cn id=1406 lang=python3
#
# [1406] 石子游戏 III
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        best = [0, 0, 0, 0]
        for index in range(len(stoneValue) - 1, -1, -1):
            best[index % 4] = max(
                stoneValue[index] - best[(index + 1) % 4],
                (
                    stoneValue[index] + (stoneValue[index + 1] - best[(index + 2) % 4])
                    if index + 1 < len(stoneValue)
                    else stoneValue[index]
                ),
                stoneValue[index]
                + (stoneValue[index + 1] if index + 1 < len(stoneValue) else 0)
                + (
                    stoneValue[index + 2] - best[(index + 3) % 4]
                    if index + 2 < len(stoneValue)
                    else 0
                ),
            )
        score = best[0]
        return "Alice" if score > 0 else "Bob" if score < 0 else "Tie"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.stoneGameIII, ([-1, 2, -3, 4, -5],), "Bob"),
        (solution.stoneGameIII, ([1, 2, 3, 7],), "Bob"),
        (solution.stoneGameIII, ([1, 2, 3, -9],), "Alice"),
        (solution.stoneGameIII, ([1, 2, 3, 6],), "Tie"),
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
