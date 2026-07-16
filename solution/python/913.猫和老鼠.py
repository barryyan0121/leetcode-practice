#
# @lc app=leetcode.cn id=913 lang=python3
#
# [913] 猫和老鼠
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        result = [[[0, 0] for _ in range(n)] for _ in range(n)]
        degree = [
            [
                [len(graph[mouse]), len(graph[cat]) - (0 in graph[cat])]
                for cat in range(n)
            ]
            for mouse in range(n)
        ]
        queue = deque()

        for cat in range(1, n):
            for turn in range(2):
                result[0][cat][turn] = 1
                result[cat][cat][turn] = 2
                queue.append((0, cat, turn))
                queue.append((cat, cat, turn))

        while queue:
            mouse, cat, turn = queue.popleft()
            winner = result[mouse][cat][turn]
            if turn == 0:
                parents = ((mouse, previous, 1) for previous in graph[cat] if previous)
            else:
                parents = ((previous, cat, 0) for previous in graph[mouse])
            for previous_mouse, previous_cat, previous_turn in parents:
                if result[previous_mouse][previous_cat][previous_turn]:
                    continue
                if winner == previous_turn + 1:
                    result[previous_mouse][previous_cat][previous_turn] = winner
                    queue.append((previous_mouse, previous_cat, previous_turn))
                else:
                    degree[previous_mouse][previous_cat][previous_turn] -= 1
                    if degree[previous_mouse][previous_cat][previous_turn] == 0:
                        result[previous_mouse][previous_cat][previous_turn] = (
                            2 - previous_turn
                        )
                        queue.append((previous_mouse, previous_cat, previous_turn))

        return result[1][2][0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.catMouseGame,
            ([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]],),
            0,
        ),
        (solution.catMouseGame, ([[1, 3], [0], [3], [0, 2]],), 1),
        (solution.catMouseGame, ([[2], [2], [0, 1]],), 2),
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
