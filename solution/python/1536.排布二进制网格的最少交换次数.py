# @lc app=leetcode.cn id=1536 lang=python3


class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trailing = []
        for row in grid:
            zeros = 0
            for value in reversed(row):
                if value:
                    break
                zeros += 1
            trailing.append(zeros)
        swaps = 0
        for row in range(n):
            required = n - row - 1
            found = next(
                (index for index in range(row, n) if trailing[index] >= required), None
            )
            if found is None:
                return -1
            swaps += found - row
            trailing[row + 1 : found + 1] = trailing[row:found]
        return swaps


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minSwaps, ([[0, 0, 1], [1, 1, 0], [1, 0, 0]],), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1536 题 "排布二进制网格的最少交换次数" 所有测试用例通过')
