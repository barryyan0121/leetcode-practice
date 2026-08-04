from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        odd = max(count for count in counts.values() if count % 2)
        even = min(count for count in counts.values() if count % 2 == 0)
        return odd - even


if __name__ == "__main__":
    test_cases = [
        (("aaaaabbc",), 3),
        (("abcabcab",), 1),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().maxDifference(s) == expected
