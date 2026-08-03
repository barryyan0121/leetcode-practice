class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = {char: index for index, char in enumerate(keyboard)}
        current = 0
        total = 0
        for char in word:
            total += abs(positions[char] - current)
            current = positions[char]
        return total


if __name__ == "__main__":
    test_cases = [("abcdefghijklmnopqrstuvwxyz", "cba", 4)]
    for _, (keyboard, word, expected) in enumerate(test_cases):
        assert Solution().calculateTime(keyboard, word) == expected
