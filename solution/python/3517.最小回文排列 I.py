class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = "".join(sorted(s[: len(s) // 2]))
        middle = s[len(s) // 2] if len(s) % 2 else ""
        return half + middle + half[::-1]


if __name__ == "__main__":
    test_cases = [
        ("z", "z"),
        ("babab", "abbba"),
        ("daccad", "acddca"),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().smallestPalindrome(s) == expected
