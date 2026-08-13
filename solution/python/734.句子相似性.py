"""734. 句子相似性"""


class Solution:
    def areSentencesSimilar(
        self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs = {tuple(pair) for pair in similarPairs}
        return all(
            left == right or (left, right) in pairs or (right, left) in pairs
            for left, right in zip(sentence1, sentence2)
        )


if __name__ == "__main__":
    assert Solution().areSentencesSimilar(
        ["great", "acting", "skills"],
        ["fine", "drama", "talent"],
        [["great", "fine"], ["drama", "acting"], ["skills", "talent"]],
    )
    assert not Solution().areSentencesSimilar(
        ["great"], ["doubleplus", "good"], [["great", "doubleplus"]]
    )
