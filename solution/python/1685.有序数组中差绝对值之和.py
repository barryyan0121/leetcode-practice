# @lc app=leetcode.cn id=1685 lang=python3


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        prefix = answer = 0
        result = []
        for index, value in enumerate(nums):
            result.append(
                value * index - prefix + total - prefix - value * (len(nums) - index)
            )
            prefix += value
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.getSumAbsoluteDifferences, ([2, 3, 5],), [4, 3, 5]),
        (solution.getSumAbsoluteDifferences, ([1, 4, 6, 8, 10],), [24, 15, 13, 15, 21]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1685 题 "有序数组中差绝对值之和" 所有测试用例通过')
