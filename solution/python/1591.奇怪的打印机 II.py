# @lc app=leetcode.cn id=1591 lang=python3


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        colors = set(value for row in targetGrid for value in row)
        bounds = {
            color: [len(targetGrid), len(targetGrid[0]), 0, 0] for color in colors
        }
        for row, values in enumerate(targetGrid):
            for col, color in enumerate(values):
                bounds[color] = [
                    min(bounds[color][0], row),
                    min(bounds[color][1], col),
                    max(bounds[color][2], row),
                    max(bounds[color][3], col),
                ]
        graph = {color: set() for color in colors}
        indegree = {color: 0 for color in colors}
        for color, (top, left, bottom, right) in bounds.items():
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    other = targetGrid[row][col]
                    if other != color and color not in graph[other]:
                        graph[other].add(color)
                        indegree[color] += 1
        stack = [color for color in colors if indegree[color] == 0]
        seen = 0
        while stack:
            color = stack.pop()
            seen += 1
            for other in graph[color]:
                indegree[other] -= 1
                if indegree[other] == 0:
                    stack.append(other)
        return seen == len(colors)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isPrintable, ([[1, 1, 1], [1, 1, 1]],), True),
        (solution.isPrintable, ([[1, 2, 1], [2, 1, 2]],), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1591 题 "奇怪的打印机 II" 所有测试用例通过')
