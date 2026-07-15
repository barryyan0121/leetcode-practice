#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = {tuple(obstacle) for obstacle in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        x = y = answer = 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) in blocked:
                        break
                    x += dx
                    y += dy
                    answer = max(answer, x * x + y * y)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.robotSim, ([4, -1, 3], []), 25),
        (solution.robotSim, ([4, -1, 4, -2, 4], [[2, 4]]), 65),
        (solution.robotSim, ([6, -1, -1, 6], []), 36),
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
