class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if any(not character.isalnum() for character in word):
            return False
        lowercase = word.lower()
        return any(character in "aeiou" for character in lowercase) and any(
            character.isalpha() and character not in "aeiou" for character in lowercase
        )


if __name__ == "__main__":
    test_cases = [("234Adas", True), ("b3", False), ("a3$e", False)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().isValid(word) == expected
