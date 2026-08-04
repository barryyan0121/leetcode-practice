class Solution:
    def findMinimumTime(self, strength: list[int], k: int) -> int:
        size = len(strength)
        infinity = 10**18
        dp = [infinity] * (1 << size)
        dp[0] = 0
        for mask in range(1 << size):
            opened = mask.bit_count()
            energy_factor = 1 + opened * k
            for index, required in enumerate(strength):
                if mask & (1 << index) == 0:
                    next_mask = mask | (1 << index)
                    time = (required + energy_factor - 1) // energy_factor
                    dp[next_mask] = min(dp[next_mask], dp[mask] + time)
        return dp[-1]


if __name__ == "__main__":
    test_cases = [
        (([3, 4, 1], 1), 4),
        (([2, 5, 4], 2), 5),
    ]
    for _, ((strength, k), expected) in enumerate(test_cases):
        assert Solution().findMinimumTime(strength, k) == expected
