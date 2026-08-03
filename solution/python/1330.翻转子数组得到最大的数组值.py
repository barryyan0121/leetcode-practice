# @lc app=leetcode.cn id=1330 lang=python3

from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = sum(abs(nums[index] - nums[index - 1]) for index in range(1, len(nums)))
        gain = 0
        low, high = float("inf"), float("-inf")
        for left, right in zip(nums, nums[1:]):
            low = min(low, max(left, right))
            high = max(high, min(left, right))
            gain = max(gain, 2 * (high - low))
            gain = max(gain, abs(nums[0] - right) - abs(left - right))
            gain = max(gain, abs(nums[-1] - left) - abs(left - right))
        return base + gain


if __name__ == "__main__":
    test_cases = [
        (Solution().maxValueAfterReverse, ([2, 3, 1, 5, 4],), 10),
        (Solution().maxValueAfterReverse, ([2, 4, 9, 24, 2, 1, 10],), 68),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1330 题 "翻转子数组得到最大的数组值" 所有测试用例通过')
