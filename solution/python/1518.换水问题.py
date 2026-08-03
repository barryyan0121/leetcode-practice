# @lc app=leetcode.cn id=1518 lang=python3


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numWaterBottles, (9, 3), 13)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1518 题 "换水问题" 所有测试用例通过')
