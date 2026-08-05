from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        return max((counts[c] for c in "aeiou"), default=0) + max(
            (counts[c] for c in counts if c not in "aeiou"), default=0
        )


if __name__ == "__main__":
    test_cases = [("successes", 6), ("aeiaeia", 3)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().maxFreqSum(s) == expected
