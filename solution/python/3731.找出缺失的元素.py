# @lc app=leetcode.cn id=3731 lang=python3


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        present = set(nums)
        return [
            value for value in range(min(nums), max(nums) + 1) if value not in present
        ]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findMissingElements, ([1, 4, 2, 5],), [3]),
        (solution.findMissingElements, ([7, 8, 6, 9],), []),
        (solution.findMissingElements, ([5, 1],), [2, 3, 4]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 3731 题 "找出缺失的元素" 所有测试用例通过')
