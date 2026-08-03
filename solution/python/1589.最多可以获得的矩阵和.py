# @lc app=leetcode.cn id=1589 lang=python3


class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        mod = 10**9 + 7
        count = [0] * (len(nums) + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for index in range(1, len(nums)):
            count[index] += count[index - 1]
        return sum(a * b for a, b in zip(sorted(nums), sorted(count[:-1]))) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxSumRangeQuery, ([1, 2, 3, 4, 5], [[1, 3], [0, 1]]), 19)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1589 题 "最多可以获得的矩阵和" 所有测试用例通过')
