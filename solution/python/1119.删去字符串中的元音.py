class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join(char for char in s if char not in "aeiou")


if __name__ == "__main__":
    test_cases = [
        ("leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs"),
        ("aeiou", ""),
        ("bcdfg", "bcdfg"),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().removeVowels(s) == expected
