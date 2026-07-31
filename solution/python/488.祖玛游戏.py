#
# @lc app=leetcode.cn id=488 lang=python3
# @lcpr version=30203
#
# [488] 祖玛游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import Counter
from functools import cache
from common.node import *


# @lc code=start
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def shrink(s: str) -> str:
            while True:
                for i in range(len(s)):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        s = s[:i] + s[j:]
                        break
                else:
                    return s

        colors = "RYBGW"
        initial = tuple(Counter(hand)[color] for color in colors)

        @cache
        def dfs(s: str, counts: tuple[int, ...]) -> int:
            best = float("inf")
            for color_index, color in enumerate(colors):
                if not counts[color_index]:
                    continue
                next_counts = list(counts)
                next_counts[color_index] -= 1
                for index in range(len(s) + 1):
                    left = s[index - 1] if index else ""
                    right = s[index] if index < len(s) else ""
                    if (left == color or right == color) and left != color:
                        pass
                    elif left != right:
                        continue
                    nxt = shrink(s[:index] + color + s[index:])
                    if not nxt:
                        return 1
                    steps = dfs(nxt, tuple(next_counts))
                    if steps != -1:
                        best = min(best, steps + 1)
            return -1 if best == float("inf") else best

        return dfs(board, initial)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findMinStep, ("WRRBBW", "RB"), -1),
        (solution.findMinStep, ("WWRRBBWW", "WRBRW"), 2),
        (solution.findMinStep, ("G", "GGGGG"), 2),
        (solution.findMinStep, ("RRWWRRBBRR", "WB"), 2),
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
# WRRBBW\nRB\n
# @lcpr case=end

#
