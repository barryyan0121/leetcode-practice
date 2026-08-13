class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for index in range(len(s)):
            if s[index] == s[~index]:
                return index
        return -1


if __name__ == "__main__":
    test_cases = [
        ("abcacbd", 1),
        ("abc", 1),
        ("abcdab", -1),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().firstMatchingIndex(s) == expected
