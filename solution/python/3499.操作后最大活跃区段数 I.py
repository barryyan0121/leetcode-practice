from itertools import groupby


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        groups = [(digit, sum(1 for _ in group)) for digit, group in groupby(s)]
        gain = max(
            (
                groups[index - 1][1] + groups[index + 1][1]
                for index in range(1, len(groups) - 1)
                if groups[index][0] == "1"
            ),
            default=0,
        )
        return s.count("1") + gain


if __name__ == "__main__":
    test_cases = [
        ("01", 1),
        ("0100", 4),
        ("1000100", 7),
        ("01010", 4),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().maxActiveSectionsAfterTrade(s) == expected
