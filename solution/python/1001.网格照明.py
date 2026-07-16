#
# @lc app=leetcode.cn id=1001 lang=python3
#
# [1001] 网格照明
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def gridIllumination(
        self, n: int, lamps: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        active = {tuple(lamp) for lamp in lamps}
        rows = Counter(row for row, _ in active)
        columns = Counter(column for _, column in active)
        diagonals = Counter(row - column for row, column in active)
        anti_diagonals = Counter(row + column for row, column in active)
        result = []
        for row, column in queries:
            result.append(
                int(
                    bool(
                        rows[row]
                        or columns[column]
                        or diagonals[row - column]
                        or anti_diagonals[row + column]
                    )
                )
            )
            for next_row in range(max(0, row - 1), min(n, row + 2)):
                for next_column in range(max(0, column - 1), min(n, column + 2)):
                    lamp = (next_row, next_column)
                    if lamp in active:
                        active.remove(lamp)
                        rows[next_row] -= 1
                        columns[next_column] -= 1
                        diagonals[next_row - next_column] -= 1
                        anti_diagonals[next_row + next_column] -= 1
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.gridIllumination, (5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]), [1, 0]),
        (solution.gridIllumination, (5, [[0, 0], [4, 4]], [[1, 1], [1, 1]]), [1, 1]),
        (solution.gridIllumination, (5, [[0, 0], [0, 0]], [[0, 0], [0, 0]]), [1, 0]),
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
