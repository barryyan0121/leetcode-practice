#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        return sorted(
            ([row, column] for row in range(rows) for column in range(cols)),
            key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter),
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.allCellsDistOrder, (1, 2, 0, 0), [[0, 0], [0, 1]]),
        (solution.allCellsDistOrder, (2, 2, 0, 1), [[0, 1], [0, 0], [1, 1], [1, 0]]),
        (solution.allCellsDistOrder, (1, 1, 0, 0), [[0, 0]]),
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
