class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = [len(word)] * 26
        last_lower = [-1] * 26
        for index, character in enumerate(word):
            if character.islower():
                last_lower[ord(character) - ord("a")] = index
            else:
                first_upper[ord(character) - ord("A")] = min(
                    first_upper[ord(character) - ord("A")], index
                )
        return sum(
            last_lower[index] >= 0
            and first_upper[index] < len(word)
            and last_lower[index] < first_upper[index]
            for index in range(26)
        )


if __name__ == "__main__":
    test_cases = [("aaAbcBC", 3), ("abcABC", 3), ("aAAbBc", 2)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().numberOfSpecialChars(word) == expected
