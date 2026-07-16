#
# @lc app=leetcode.cn id=957 lang=python3
#
# [957] N 天后的牢房
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state = tuple(cells)
        seen = {}
        while n:
            if state in seen:
                cycle = seen[state] - n
                n %= cycle
                seen.clear()
                if not n:
                    break
            seen[state] = n
            state = (
                (0,)
                + tuple(
                    int(state[index - 1] == state[index + 1]) for index in range(1, 7)
                )
                + (0,)
            )
            n -= 1
        return list(state)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.prisonAfterNDays,
            ([0, 1, 0, 1, 1, 0, 0, 1], 7),
            [0, 0, 1, 1, 0, 0, 0, 0],
        ),
        (
            solution.prisonAfterNDays,
            ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000),
            [0, 0, 1, 1, 1, 1, 1, 0],
        ),
        (
            solution.prisonAfterNDays,
            ([1, 1, 1, 0, 1, 1, 1, 1], 0),
            [1, 1, 1, 0, 1, 1, 1, 1],
        ),
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
