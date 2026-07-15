#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]
        while stack:
            for room in rooms[stack.pop()]:
                if room not in visited:
                    visited.add(room)
                    stack.append(room)
        return len(visited) == len(rooms)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canVisitAllRooms, ([[1], [2], [3], []],), True),
        (solution.canVisitAllRooms, ([[1, 3], [3, 0, 1], [2], [0]],), False),
        (solution.canVisitAllRooms, ([[]],), True),
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
