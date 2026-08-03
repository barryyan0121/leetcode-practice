# @lc app=leetcode.cn id=1582 lang=python3


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [
            sum(mat[row][col] for row in range(len(mat))) for col in range(len(mat[0]))
        ]
        return sum(
            mat[row][col] == 1 and rows[row] == cols[col] == 1
            for row in range(len(mat))
            for col in range(len(mat[0]))
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numSpecial, ([[1, 0, 0], [0, 0, 1], [1, 0, 0]],), 1)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1582 题 "二进制矩阵中的特殊位置" 所有测试用例通过')
