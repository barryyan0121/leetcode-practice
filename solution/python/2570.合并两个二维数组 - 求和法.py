# @lc app=leetcode.cn id=2570 lang=python3


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        values = {}
        for key, value in nums1 + nums2:
            values[key] = values.get(key, 0) + value
        return [[key, values[key]] for key in sorted(values)]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.mergeArrays,
            ([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]),
            [[1, 6], [2, 3], [3, 2], [4, 6]],
        ),
        (solution.mergeArrays, ([[1, 1]], [[2, 2]]), [[1, 1], [2, 2]]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2570 题 "合并两个二维数组 - 求和法" 所有测试用例通过')
