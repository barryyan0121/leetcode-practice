#
# @lc app=leetcode.cn id=289 lang=python3
# @lcpr version=30203
#
# [289] 生命游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def live_neighbors(i: int, j: int) -> int:
            cnt = 0
            for x in range(max(0, i - 1), min(m, i + 2)):
                for y in range(max(0, j - 1), min(n, j + 2)):
                    cnt += board[x][y] & 1
            return cnt - (board[i][j] & 1)

        for i in range(m):
            for j in range(n):
                cnt = live_neighbors(i, j)
                if board[i][j] == 1 and cnt in (2, 3):
                    board[i][j] |= 2
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.gameOfLife,
            [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        (solution.gameOfLife, [[[1, 1], [1, 0]]], [[1, 1], [1, 1]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            board = args[0]
            func(*args)
            assert board == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {board}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {board}"
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
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

#
