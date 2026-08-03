# @lc app=leetcode.cn id=2401 lang=python3


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        mask = 0
        left = 0
        answer = 0
        for right, value in enumerate(nums):
            while mask & value:
                mask ^= nums[left]
                left += 1
            mask |= value
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestNiceSubarray, ([1, 3, 8, 48, 10],), 3),
        (solution.longestNiceSubarray, ([3, 1, 5, 11, 13],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2401 题 "最长优雅子数组" 所有测试用例通过')
