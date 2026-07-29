class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = sum(a == "x" and b == "y" for a, b in zip(s1, s2))
        yx = sum(a == "y" and b == "x" for a, b in zip(s1, s2))
        return -1 if (xy + yx) % 2 else xy // 2 + yx // 2 + 2 * (xy % 2)


if __name__ == "__main__":
    test_cases = [("xx", "yy", 1), ("xy", "yx", 2), ("xx", "xy", -1)]
    for _, (s1, s2, expected) in enumerate(test_cases):
        assert Solution().minimumSwap(s1, s2) == expected
