#
# @lc app=leetcode.cn id=675 lang=python3
# @lcpr version=30203
#
# [675] 为高尔夫比赛砍树
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = sorted(
            (forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1
        )

        def dist(sx: int, sy: int, tx: int, ty: int) -> int:
            queue = deque([(sx, sy, 0)])
            seen = {(sx, sy)}
            while queue:
                x, y, step = queue.popleft()
                if (x, y) == (tx, ty):
                    return step
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and forest[nx][ny]
                        and (nx, ny) not in seen
                    ):
                        seen.add((nx, ny))
                        queue.append((nx, ny, step + 1))
            return -1

        ans = x = y = 0
        for _, tx, ty in trees:
            step = dist(x, y, tx, ty)
            if step < 0:
                return -1
            ans += step
            x, y = tx, ty
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.cutOffTree, ([[1, 2, 3], [0, 0, 4], [7, 6, 5]],), 6),
        (solution.cutOffTree, ([[1, 2, 3], [0, 0, 0], [7, 6, 5]],), -1),
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
