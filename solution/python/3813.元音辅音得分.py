"""3813. 元音辅音得分"""


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = sum(char in "aeiou" for char in s)
        consonants = sum(char.isalpha() and char not in "aeiou" for char in s)
        return vowels // consonants if consonants else 0


if __name__ == "__main__":
    test_cases = [(("cooear",), 2), (("axeyizou",), 1), (("au 123",), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().vowelConsonantScore(*args) == expected
