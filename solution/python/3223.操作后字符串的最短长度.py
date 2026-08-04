from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(2 if count % 2 == 0 else 1 for count in Counter(s).values())


if __name__ == "__main__":
    test_cases = [("abaacbcbb", 5), ("aa", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minimumLength(s) == expected
