# @lc app=leetcode.cn id=1438 lang=python3

from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        increasing, decreasing = deque(), deque()
        left = result = 0
        for right, value in enumerate(nums):
            while increasing and nums[increasing[-1]] > value:
                increasing.pop()
            while decreasing and nums[decreasing[-1]] < value:
                decreasing.pop()
            increasing.append(right)
            decreasing.append(right)
            while nums[decreasing[0]] - nums[increasing[0]] > limit:
                if increasing[0] == left:
                    increasing.popleft()
                if decreasing[0] == left:
                    decreasing.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.longestSubarray, ([8, 2, 4, 7], 4), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1438 题 "绝对差不超过限制的最长连续子数组" 所有测试用例通过')
