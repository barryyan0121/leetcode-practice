"""2047. 句子中的有效单词数"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(token: str) -> bool:
            hyphen = 0
            for index, char in enumerate(token):
                if char.isdigit():
                    return False
                if char == "-":
                    if (
                        hyphen
                        or index == 0
                        or index == len(token) - 1
                        or not token[index - 1].islower()
                        or not token[index + 1].islower()
                    ):
                        return False
                    hyphen = 1
                elif char in "!.," and index != len(token) - 1:
                    return False
                elif char not in "!.," and not char.islower():
                    return False
            return True

        return sum(valid(token) for token in sentence.split())


if __name__ == "__main__":
    test_cases = [(("cat and  dog",), 3), (("!this  1-s b8d!",), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countValidWords(*args) == expected
