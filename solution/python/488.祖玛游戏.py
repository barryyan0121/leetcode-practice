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
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = "RYBGW"
        hand_count = Counter(hand)
        start = tuple(hand_count.get(c, 0) for c in colors)

        def shrink(s: str) -> str:
            changed = True
            while changed:
                changed = False
                i = 0
                parts = []
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        parts.append(s[i:j])
                    i = j
                s = "".join(parts)
            return s

        @lru_cache(None)
        def dfs(s: str, hand_state: Tuple[int, ...]) -> int:
            s = shrink(s)
            if not s:
                return 0
            counts = list(hand_state)
            ans = float("inf")
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                idx = colors.index(s[i])
                need = 3 - (j - i)
                if 0 < need <= counts[idx]:
                    counts[idx] -= need
                    nxt = dfs(s[:i] + s[j:], tuple(counts))
                    if nxt != -1:
                        ans = min(ans, nxt + need)
                    counts[idx] += need
                i = j
            return -1 if ans == float("inf") else ans

        return dfs(board, start)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findMinStep, ("WRRBBW", "RB"), -1),
        (solution.findMinStep, ("WWRRBBWW", "WRBRW"), 2),
        (solution.findMinStep, ("G", "GGGGG"), 2),
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
