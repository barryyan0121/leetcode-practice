# @lc app=leetcode.cn id=1537 lang=python3


class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        first = second = 0
        index = other = 0
        mod = 10**9 + 7
        while index < len(nums1) or other < len(nums2):
            if other == len(nums2) or (
                index < len(nums1) and nums1[index] < nums2[other]
            ):
                first += nums1[index]
                index += 1
            elif index == len(nums1) or nums2[other] < nums1[index]:
                second += nums2[other]
                other += 1
            else:
                first = second = max(first, second) + nums1[index]
                index += 1
                other += 1
        return max(first, second) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxSum, ([2, 4, 5, 8, 10], [4, 6, 8, 9]), 30)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1537 题 "最大得分" 所有测试用例通过')
