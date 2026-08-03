# @lc app=leetcode.cn id=2453 lang=python3

from collections import Counter


class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        counts = Counter(value % space for value in nums)
        best_count = max(counts.values())
        return min(value for value in nums if counts[value % space] == best_count)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.destroyTargets, ([3, 7, 8, 1, 1, 5], 2), 1),
        (solution.destroyTargets, ([1, 2, 3, 4, 5, 6], 3), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2453 题 "摧毁一系列目标" 所有测试用例通过')
