#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#

from collections import deque
import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        blocked = {tuple(point) for point in blocked}
        limit = len(blocked) * (len(blocked) - 1) // 2

        def escapes(start: List[int], end: List[int]) -> bool:
            queue = deque([tuple(start)])
            seen = {tuple(start)}
            while queue and len(seen) <= limit:
                row, column = queue.popleft()
                if (row, column) == tuple(end):
                    return True
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    point = (next_row, next_column)
                    if (
                        0 <= next_row < 10**6
                        and 0 <= next_column < 10**6
                        and point not in blocked
                        and point not in seen
                    ):
                        seen.add(point)
                        queue.append(point)
            return len(seen) > limit

        return escapes(source, target) and escapes(target, source)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isEscapePossible, ([], [0, 0], [999999, 999999]), True),
        (solution.isEscapePossible, ([[0, 1], [1, 0]], [0, 0], [0, 2]), False),
        (
            solution.isEscapePossible,
            ([[10, 9], [9, 10], [10, 11], [11, 10]], [10, 10], [0, 0]),
            False,
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
