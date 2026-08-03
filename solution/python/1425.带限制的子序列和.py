# @lc app=leetcode.cn id=1425 lang=python3

from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        window = deque()
        best = nums[:]
        for index, value in enumerate(nums):
            if window:
                best[index] = value + max(0, best[window[0]])
            while window and best[window[-1]] <= best[index]:
                window.pop()
            window.append(index)
            while window and window[0] <= index - k:
                window.popleft()
        return max(best)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.constrainedSubsetSum, ([10, 2, -10, 5, 20], 2), 37)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1425 题 "带限制的子序列和" 所有测试用例通过')
