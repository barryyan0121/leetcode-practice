# @lc app=leetcode.cn id=1508 lang=python3


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        values = []
        for start in range(n):
            total = 0
            for end in range(start, n):
                total += nums[end]
                values.append(total)
        values.sort()
        return sum(values[left - 1 : right]) % (10**9 + 7)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.rangeSum, ([1, 2, 3, 4], 4, 1, 5), 13)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1508 题 "子数组和排序后的区间和" 所有测试用例通过')
