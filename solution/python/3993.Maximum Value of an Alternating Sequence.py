"""3993. Maximum Value of an Alternating Sequence"""


class Solution:
    def maxValue(self, n: int, s: int, m: int) -> int:
        peaks = n // 2
        return s + peaks * m - max(0, peaks - 1)


if __name__ == "__main__":
    test_cases = [
        ((4, 3, 5), 12),
        ((2, 4, 3), 7),
        ((1, 9, 8), 9),
        ((5, 1, 2), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxValue(*args) == expected
