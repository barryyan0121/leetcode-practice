#
# @lc app=leetcode.cn id=403 lang=python3
# @lcpr version=30203
#
# [403] 青蛙过河
#

import sys
import os
from functools import lru_cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        target = stones[-1]

        @lru_cache(None)
        def dfs(pos: int, jump: int) -> bool:
            if pos == target:
                return True
            for nj in (jump - 1, jump, jump + 1):
                if nj > 0 and pos + nj in stone_set:
                    if dfs(pos + nj, nj):
                        return True
            return False

        return dfs(0, 0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.canCross, [[0, 1, 3, 5, 6, 8, 12, 17]], True),
        (solution.canCross, [[0, 1, 2, 3, 4, 8, 9, 11]], False),
        (solution.canCross, [[0]], True),
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
# [0,1,3,5,6,8,12,17]\n
# @lcpr case=end

#
