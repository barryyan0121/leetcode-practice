#
# @lc app=leetcode.cn id=749 lang=python3
#
# [749] 隔离病毒
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows, columns = len(isInfected), len(isInfected[0])
        answer = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while True:
            regions, frontiers, walls = [], [], []
            visited = set()
            for row in range(rows):
                for column in range(columns):
                    if isInfected[row][column] != 1 or (row, column) in visited:
                        continue
                    region, frontier = set(), set()
                    wall_count = 0
                    stack = [(row, column)]
                    visited.add((row, column))
                    while stack:
                        current_row, current_column = stack.pop()
                        region.add((current_row, current_column))
                        for row_step, column_step in directions:
                            next_row = current_row + row_step
                            next_column = current_column + column_step
                            if not (
                                0 <= next_row < rows and 0 <= next_column < columns
                            ):
                                continue
                            if isInfected[next_row][next_column] == 0:
                                frontier.add((next_row, next_column))
                                wall_count += 1
                            elif (
                                isInfected[next_row][next_column] == 1
                                and (next_row, next_column) not in visited
                            ):
                                visited.add((next_row, next_column))
                                stack.append((next_row, next_column))
                    regions.append(region)
                    frontiers.append(frontier)
                    walls.append(wall_count)

            if not regions:
                break
            quarantine = max(
                range(len(frontiers)), key=lambda index: len(frontiers[index])
            )
            if not frontiers[quarantine]:
                break
            answer += walls[quarantine]
            for index, region in enumerate(regions):
                if index == quarantine:
                    for row, column in region:
                        isInfected[row][column] = -1
                else:
                    for row, column in frontiers[index]:
                        isInfected[row][column] = 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.containVirus,
            (
                [
                    [0, 1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ],
            ),
            10,
        ),
        (solution.containVirus, ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), 4),
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
