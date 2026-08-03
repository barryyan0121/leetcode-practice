class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        modulus = 1_000_000_007
        dp = [0] * (k + 1)
        dp[0] = 1
        for number in nums:
            for total in range(k, number - 1, -1):
                dp[total] = (2 * dp[total] + dp[total - number]) % modulus
            for total in range(min(number, k + 1)):
                dp[total] = dp[total] * 2 % modulus
        return dp[k]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 3), 6),
        (([2, 3, 3], 5), 4),
        (([1, 2, 3], 7), 0),
        (([3], 1), 0),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().sumOfPower(nums, k) == expected
