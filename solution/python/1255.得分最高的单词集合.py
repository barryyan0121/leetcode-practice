from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        available = Counter(letters)

        def search(index: int) -> int:
            if index == len(words):
                return 0
            answer = search(index + 1)
            word = Counter(words[index])
            if word <= available:
                available.subtract(word)
                answer = max(
                    answer,
                    sum(score[ord(char) - 97] * count for char, count in word.items())
                    + search(index + 1),
                )
                available.update(word)
            return answer

        return search(0)


if __name__ == "__main__":
    test_cases = [
        (
            (
                ["dog", "cat", "dad", "good"],
                list("aaccdddg oo".replace(" ", "")),
                [1, 0, 9, 5, 0, 0, 3] + [0] * 7 + [2] + [0] * 11,
            ),
            23,
        )
    ]
    for _, ((words, letters, score), expected) in enumerate(test_cases):
        assert Solution().maxScoreWords(words, letters, score) == expected
