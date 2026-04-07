#
# @lc app=leetcode.cn id=489 lang=python3
# @lcpr version=30203
#
# [489] 扫地机器人
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


class Robot:  # pragma: no cover
    def move(self) -> bool:
        raise NotImplementedError

    def turnLeft(self) -> None:
        raise NotImplementedError

    def turnRight(self) -> None:
        raise NotImplementedError

    def clean(self) -> None:
        raise NotImplementedError


# @lc code=start
class Solution:
    def cleanRoom(self, robot: "Robot") -> None:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(x: int, y: int, d: int) -> None:
            visited.add((x, y))
            robot.clean()
            for k in range(4):
                nd = (d + k) % 4
                nx, ny = x + dirs[nd][0], y + dirs[nd][1]
                if (nx, ny) not in visited and robot.move():
                    dfs(nx, ny, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dfs(0, 0, 0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    class MockRobot:
        def __init__(self, room: List[List[int]], row: int, col: int):
            self.room = room
            self.row = row
            self.col = col
            self.dir = 0
            self.cleaned = set()
            self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def move(self) -> bool:
            dr, dc = self.dirs[self.dir]
            nr, nc = self.row + dr, self.col + dc
            if (
                0 <= nr < len(self.room)
                and 0 <= nc < len(self.room[0])
                and self.room[nr][nc] == 0
            ):
                self.row, self.col = nr, nc
                return True
            return False

        def turnLeft(self) -> None:
            self.dir = (self.dir + 3) % 4

        def turnRight(self) -> None:
            self.dir = (self.dir + 1) % 4

        def clean(self) -> None:
            self.cleaned.add((self.row, self.col))

    def run_case(room: List[List[int]], row: int, col: int) -> Set[Tuple[int, int]]:
        robot = MockRobot(room, row, col)
        solution.cleanRoom(robot)
        q = deque([(row, col)])
        seen = {(row, col)}
        reachable = set()
        while q:
            r, c = q.popleft()
            reachable.add((r, c))
            for dr, dc in robot.dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < len(room)
                    and 0 <= nc < len(room[0])
                    and room[nr][nc] == 0
                    and (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    q.append((nr, nc))
        assert robot.cleaned == reachable
        return robot.cleaned

    test_cases = [
        (
            run_case,
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 0),
            {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)},
        ),
        (run_case, ([[0]], 0, 0), {(0, 0)}),
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
# [[0]]\n0\n0\n
# @lcpr case=end

#
