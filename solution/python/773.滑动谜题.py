#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = "".join(map(str, board[0] + board[1]))
        target = "123450"
        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero = state.index("0")
            for neighbor in neighbors[zero]:
                values = list(state)
                values[zero], values[neighbor] = values[neighbor], values[zero]
                next_state = "".join(values)
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, moves + 1))
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.slidingPuzzle, ([[1, 2, 3], [4, 0, 5]],), 1),
        (solution.slidingPuzzle, ([[1, 2, 3], [5, 4, 0]],), -1),
        (solution.slidingPuzzle, ([[4, 1, 2], [5, 0, 3]],), 5),
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
