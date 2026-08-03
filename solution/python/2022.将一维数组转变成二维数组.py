# @lc app=leetcode.cn id=2022 lang=python3


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        return [original[row * n : (row + 1) * n] for row in range(m)]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.construct2DArray, ([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]]),
        (solution.construct2DArray, ([1, 2, 3], 1, 2), []),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2022 题 "将一维数组转变成二维数组" 所有测试用例通过')
