# @lc app=leetcode.cn id=1424 lang=python3


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        diagonals = {}
        for row, values in enumerate(nums):
            for column, value in enumerate(values):
                diagonals.setdefault(row + column, []).append(value)
        result = []
        for diagonal in sorted(diagonals):
            result.extend(reversed(diagonals[diagonal]))
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findDiagonalOrder,
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
            [1, 4, 2, 7, 5, 3, 8, 6, 9],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1424 题 "对角线遍历 II" 所有测试用例通过')
