# @lc app=leetcode.cn id=1458 lang=python3


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        negative_infinity = -(10**18)
        dp = [[negative_infinity] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for first in range(1, len(nums1) + 1):
            for second in range(1, len(nums2) + 1):
                product = nums1[first - 1] * nums2[second - 1]
                dp[first][second] = max(
                    product,
                    (
                        product + dp[first - 1][second - 1]
                        if dp[first - 1][second - 1] != negative_infinity
                        else negative_infinity
                    ),
                    dp[first - 1][second],
                    dp[first][second - 1],
                )
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxDotProduct, ([2, 1, -2, 5], [3, 0, -6]), 18)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1458 题 "两个子序列的最大点积" 所有测试用例通过')
