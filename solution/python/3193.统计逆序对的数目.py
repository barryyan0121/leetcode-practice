class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        mod = 1_000_000_007
        required = {}
        for end, inversions in requirements:
            if end in required and required[end] != inversions:
                return 0
            required[end] = inversions

        maximum = max(required.values(), default=0)
        if required.get(0, 0) != 0:
            return 0
        dp = [1] + [0] * maximum

        for end in range(1, n):
            limit = min(maximum, end * (end + 1) // 2)
            next_dp = [0] * (maximum + 1)
            window = 0
            for inversions in range(limit + 1):
                window = (window + dp[inversions]) % mod
                if inversions > end:
                    window = (window - dp[inversions - end - 1]) % mod
                next_dp[inversions] = window
            if end in required:
                target = required[end]
                if target > limit:
                    return 0
                value = next_dp[target]
                next_dp = [0] * (maximum + 1)
                next_dp[target] = value
            dp = next_dp
        return dp[required.get(n - 1, 0)] if n - 1 in required else sum(dp) % mod


if __name__ == "__main__":
    test_cases = [
        ((3, [[2, 2], [0, 0]]), 2),
        ((3, [[2, 2], [1, 1], [0, 0]]), 1),
        ((2, [[0, 0], [1, 0]]), 1),
    ]
    for _, ((n, requirements), expected) in enumerate(test_cases):
        assert Solution().numberOfPermutations(n, requirements) == expected
