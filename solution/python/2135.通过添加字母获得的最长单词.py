"""2135. 通过添加字母获得的最长单词"""


class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        starts = {"".join(sorted(word)) for word in startWords}
        return sum(
            any(
                "".join(sorted(word[:i] + word[i + 1 :])) in starts
                for i in range(len(word))
            )
            for word in targetWords
        )


if __name__ == "__main__":
    test_cases = [((["ant", "act", "tack"], ["tack", "act", "acti"]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().wordCount(*args) == expected
