#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.exist,
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
            ),
            True,
        ),
        (
            solution.exist,
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
            True,
        ),
        (
            solution.exist,
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
            ),
            False,
        ),
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
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end
