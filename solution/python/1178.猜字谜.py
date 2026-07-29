from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counts = Counter()
        for word in words:
            mask = 0
            for char in set(word):
                mask |= 1 << (ord(char) - ord("a"))
            if mask.bit_count() <= 7:
                counts[mask] += 1

        answer = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord("a"))
            remaining = 0
            for char in puzzle[1:]:
                remaining |= 1 << (ord(char) - ord("a"))
            total = 0
            subset = remaining
            while True:
                total += counts[subset | first]
                if not subset:
                    break
                subset = (subset - 1) & remaining
            answer.append(total)
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
            ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
            [1, 1, 3, 2, 4, 0],
        )
    ]
    for _, (words, puzzles, expected) in enumerate(test_cases):
        assert Solution().findNumOfValidWords(words, puzzles) == expected
