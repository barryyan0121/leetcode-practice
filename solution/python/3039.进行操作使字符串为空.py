from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        maximum = max(counts.values())
        last_positions = {character: s.rfind(character) for character in counts}
        return "".join(
            character
            for index, character in enumerate(s)
            if counts[character] == maximum and last_positions[character] == index
        )


if __name__ == "__main__":
    test_cases = [("aabcbbca", "ba"), ("abcd", "abcd")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().lastNonEmptyString(s) == expected
