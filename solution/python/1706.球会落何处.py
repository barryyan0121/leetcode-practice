# @lc app=leetcode.cn id=1706 lang=python3


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        result = []
        for start in range(cols):
            column = start
            for row in range(rows):
                direction = grid[row][column]
                next_column = column + direction
                if (
                    next_column < 0
                    or next_column >= cols
                    or grid[row][next_column] != direction
                ):
                    column = -1
                    break
                column = next_column
            result.append(column)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findBall,
            (
                [
                    [1, 1, 1, -1, -1],
                    [1, 1, 1, -1, -1],
                    [-1, -1, -1, 1, 1],
                    [1, 1, 1, 1, -1],
                    [-1, -1, -1, -1, -1],
                ],
            ),
            [1, -1, -1, -1, -1],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1706 题 "球会落何处" 所有测试用例通过')
