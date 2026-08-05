"""2000. 反转单词前缀"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        return word if index < 0 else word[: index + 1][::-1] + word[index + 1 :]


if __name__ == "__main__":
    test_cases = [(("abcdefd", "d"), "dcbaefd")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().reversePrefix(*args) == expected
