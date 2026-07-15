#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

import os
import sys
from collections import deque
from typing import *


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = set(deadends)
        if "0000" in blocked:
            return -1
        queue = deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for index, digit in enumerate(state):
                for step in (-1, 1):
                    neighbor = (
                        state[:index]
                        + str((int(digit) + step) % 10)
                        + state[index + 1 :]
                    )
                    if neighbor not in blocked and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.openLock, (["0201", "0101", "0102", "1212", "2002"], "0202"), 6),
        (solution.openLock, (["8888"], "0009"), 1),
        (solution.openLock, (["0000"], "8888"), -1),
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
