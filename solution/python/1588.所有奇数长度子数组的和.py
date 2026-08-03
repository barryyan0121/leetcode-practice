# @lc app=leetcode.cn id=1588 lang=python3


class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        return sum(
            value * (((index + 1) * (len(arr) - index) + 1) // 2)
            for index, value in enumerate(arr)
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.sumOddLengthSubarrays, ([1, 4, 2, 5, 3],), 58)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1588 题 "所有奇数长度子数组的和" 所有测试用例通过')
