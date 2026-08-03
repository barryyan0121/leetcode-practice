class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = {character for character in word if character.islower()}
        uppercase = {character.lower() for character in word if character.isupper()}
        return len(lowercase & uppercase)


if __name__ == "__main__":
    test_cases = [("aaAbcBC", 3), ("abc", 0), ("abBCab", 1)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().numberOfSpecialChars(word) == expected
