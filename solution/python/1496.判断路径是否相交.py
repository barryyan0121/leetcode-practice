# @lc app=leetcode.cn id=1496 lang=python3


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        x = y = 0
        visited = {(x, y)}
        for move in path:
            dx, dy = moves[move]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.isPathCrossing, ("NESWW",), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1496 题 "判断路径是否相交" 所有测试用例通过')
