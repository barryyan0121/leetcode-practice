#
# @lc app=leetcode.cn id=353 lang=python3
# @lcpr version=30203
#
# [353] 设计推箱子游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.body = deque([(0, 0)])
        self.occupied = {(0, 0)}

    def move(self, direction: str) -> int:
        head_r, head_c = self.body[0]
        if direction == "U":
            head_r -= 1
        elif direction == "D":
            head_r += 1
        elif direction == "L":
            head_c -= 1
        else:
            head_c += 1

        if not (0 <= head_r < self.height and 0 <= head_c < self.width):
            return -1

        tail = self.body[-1]
        eating = (
            self.food_idx < len(self.food)
            and [head_r, head_c] == self.food[self.food_idx]
        )
        if not eating:
            self.body.pop()
            self.occupied.remove(tail)

        if (head_r, head_c) in self.occupied:
            return -1

        self.body.appendleft((head_r, head_c))
        self.occupied.add((head_r, head_c))
        if eating:
            self.food_idx += 1
        return self.food_idx


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_operations(width: int, height: int, food: List[List[int]], moves: List[str]) -> List[int]:
        game = SnakeGame(width, height, food)
        return [game.move(move) for move in moves]

    test_cases = [
        (
            run_operations,
            (3, 2, [[1, 2], [0, 1]], ["R", "D", "R", "U", "L", "U"]),
            [0, 0, 1, 1, 2, -1],
        ),
        (
            run_operations,
            (2, 2, [[0, 1]], ["R", "D", "L", "U"]),
            [1, 1, 1, 1],
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
# 3\n2\n[[1,2],[0,1]]\n
# @lcpr case=end
