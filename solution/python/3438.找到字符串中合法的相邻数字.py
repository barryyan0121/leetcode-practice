from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        for left, right in zip(s, s[1:]):
            if (
                left != right
                and counts[left] == int(left)
                and counts[right] == int(right)
            ):
                return left + right
        return ""


if __name__ == "__main__":
    test_cases = [
        (("2523533",), "23"),
        (("221",), "21"),
        (("22",), ""),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().findValidPair(s) == expected
