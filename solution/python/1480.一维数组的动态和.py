# @lc app=leetcode.cn id=1480 lang=python3


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for value in nums:
            total += value
            result.append(total)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.runningSum, ([1, 2, 3, 4],), [1, 3, 6, 10])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1480 题 "一维数组的动态和" 所有测试用例通过')
