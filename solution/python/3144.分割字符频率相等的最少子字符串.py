class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        infinity = len(s) + 1
        dp = [0] + [infinity] * len(s)
        for end in range(1, len(s) + 1):
            counts = [0] * 26
            distinct = 0
            maximum = 0
            for start in range(end - 1, -1, -1):
                index = ord(s[start]) - ord("a")
                if counts[index] == 0:
                    distinct += 1
                counts[index] += 1
                maximum = max(maximum, counts[index])
                if maximum * distinct == end - start:
                    dp[end] = min(dp[end], dp[start] + 1)
        return dp[-1]


if __name__ == "__main__":
    test_cases = [("fabcc", 2), ("aab", 2), ("abc", 1)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minimumSubstringsInPartition(s) == expected
