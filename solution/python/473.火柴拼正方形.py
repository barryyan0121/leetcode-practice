#
# @lc app=leetcode.cn id=473 lang=python3
# @lcpr version=30203
#
# [473] 火柴拼正方形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False

        sides = [0] * 4

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == side
            seen = set()
            for j in range(4):
                if sides[j] in seen or sides[j] + matchsticks[i] > side:
                    continue
                seen.add(sides[j])
                sides[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[j] -= matchsticks[i]
            return False

        return dfs(0)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.makesquare, [[1, 1, 2, 2, 2]], True),
        (solution.makesquare, [[3, 3, 3, 3, 4]], False),
        (solution.makesquare, [[1, 1, 1, 1]], True),
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
# [1,1,2,2,2]\n
# @lcpr case=end

#
