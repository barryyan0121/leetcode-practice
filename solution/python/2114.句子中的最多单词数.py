"""2114. 句子中的最多单词数"""


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(sentence.count(" ") + 1 for sentence in sentences)


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    "alice and bob love leetcode",
                    "i think so too",
                    "this is great thanks very much",
                ],
            ),
            6,
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().mostWordsFound(*args) == expected
