# @lc app=leetcode.cn id=1727 lang=python3


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        heights = [0] * len(matrix[0])
        answer = 0
        for row in matrix:
            for index, value in enumerate(row):
                heights[index] = heights[index] + 1 if value else 0
            for width, height in enumerate(sorted(heights, reverse=True), 1):
                answer = max(answer, width * height)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.largestSubmatrix, ([[0, 0, 1], [1, 1, 1], [1, 0, 1]],), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1727 题 "重新排列后的最大子矩阵" 所有测试用例通过')
