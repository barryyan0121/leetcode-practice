class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        infinity = 10**18
        dp = [[infinity] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0

        for value in nums:
            half = (value + 1) // 2
            options = [(0, 0, value), (1, 0, half)]
            if value >= k:
                options.append((0, 1, value - k))
                options.append((1, 1, (value - k + 1) // 2))
            if half >= k:
                options.append((1, 1, half - k))

            next_dp = [[infinity] * (op2 + 1) for _ in range(op1 + 1)]
            for used1 in range(op1 + 1):
                for used2 in range(op2 + 1):
                    if dp[used1][used2] == infinity:
                        continue
                    for add1, add2, result in options:
                        if used1 + add1 <= op1 and used2 + add2 <= op2:
                            next_dp[used1 + add1][used2 + add2] = min(
                                next_dp[used1 + add1][used2 + add2],
                                dp[used1][used2] + result,
                            )
            dp = next_dp
        return min(map(min, dp))


if __name__ == "__main__":
    test_cases = [
        (([2, 8, 3, 19, 3], 3, 1, 1), 23),
        (([2, 4, 3], 3, 2, 1), 3),
        (([10], 6, 1, 1), 2),
    ]
    for _, ((nums, k, op1, op2), expected) in enumerate(test_cases):
        assert Solution().minArraySum(nums, k, op1, op2) == expected
