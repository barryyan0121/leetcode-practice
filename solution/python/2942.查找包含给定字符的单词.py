"""2942. 查找包含给定字符的单词"""


class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [index for index, word in enumerate(words) if x in word]


if __name__ == "__main__":
    assert Solution().findWordsContaining(["leet", "code"], "e") == [0, 1]
