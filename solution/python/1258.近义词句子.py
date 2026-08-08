from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = {}

        def find(word: str) -> str:
            parent.setdefault(word, word)
            if parent[word] != word:
                parent[word] = find(parent[word])
            return parent[word]

        for first, second in synonyms:
            parent[find(first)] = find(second)

        groups = defaultdict(list)
        for word in parent:
            groups[find(word)].append(word)
        return [
            " ".join(sentence)
            for sentence in product(
                *(
                    sorted(groups[find(word)]) if word in parent else [word]
                    for word in text.split()
                )
            )
        ]


if __name__ == "__main__":
    test_cases = [
        (
            [["happy", "joy"], ["sad", "sorrow"]],
            "I am happy",
            ["I am happy", "I am joy"],
        )
    ]
    for _, (synonyms, text, expected) in enumerate(test_cases):
        assert Solution().generateSentences(synonyms, text) == expected
