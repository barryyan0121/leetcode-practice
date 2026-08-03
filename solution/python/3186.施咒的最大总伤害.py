from bisect import bisect_left
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        counts = Counter(power)
        values = sorted(counts)
        dp = [0] * (len(values) + 1)
        for index, value in enumerate(values):
            previous = bisect_left(values, value - 2)
            gain = value * counts[value]
            dp[index + 1] = max(dp[index], dp[previous] + gain)
        return dp[-1]


if __name__ == "__main__":
    test_cases = [([1, 1, 3, 4], 6), ([7, 1, 6, 6], 13)]
    for _, (power, expected) in enumerate(test_cases):
        assert Solution().maximumTotalDamage(power) == expected
