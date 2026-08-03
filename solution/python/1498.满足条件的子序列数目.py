# @lc app=leetcode.cn id=1498 lang=python3


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        powers = [1] * len(nums)
        for index in range(1, len(nums)):
            powers[index] = powers[index - 1] * 2 % mod
        left, right = 0, len(nums) - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + powers[right - left]) % mod
                left += 1
            else:
                right -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numSubseq, ([3, 5, 6, 7], 9), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1498 题 "满足条件的子序列数目" 所有测试用例通过')
