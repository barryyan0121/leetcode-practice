# @lc app=leetcode.cn id=2751 lang=python3


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        order = sorted(range(len(positions)), key=positions.__getitem__)
        remaining = []
        right_moving = []
        for robot in order:
            if directions[robot] == "R":
                right_moving.append(robot)
                continue
            while right_moving and healths[robot] > 0:
                other = right_moving[-1]
                if healths[other] < healths[robot]:
                    healths[robot] -= 1
                    healths[other] = 0
                    right_moving.pop()
                elif healths[other] == healths[robot]:
                    healths[robot] = 0
                    healths[other] = 0
                    right_moving.pop()
                else:
                    healths[other] -= 1
                    healths[robot] = 0
            if healths[robot] > 0:
                remaining.append(robot)
        alive = set(right_moving) | set(remaining)
        return [healths[index] for index in range(len(positions)) if index in alive]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.survivedRobotsHealths, ([1, 2], [3, 2], "RL"), [2]),
        (solution.survivedRobotsHealths, ([1, 2], [1, 1], "RL"), []),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2751 题 "机器人碰撞" 所有测试用例通过')
