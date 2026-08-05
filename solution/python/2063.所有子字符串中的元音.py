"""2063. 所有子字符串中的元音"""


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set("aeiou")
        return sum(
            (index + 1) * (len(word) - index)
            for index, char in enumerate(word)
            if char in vowels
        )


if __name__ == "__main__":
    test_cases = [("aba", 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countVowels(args) == expected
