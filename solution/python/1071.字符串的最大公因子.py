from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[: gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""


if __name__ == "__main__":
    test_cases = [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ]
    for _, (str1, str2, expected) in enumerate(test_cases):
        assert Solution().gcdOfStrings(str1, str2) == expected
