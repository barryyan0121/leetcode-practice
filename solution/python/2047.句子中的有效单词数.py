"""2047. 句子中的有效单词数"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(token: str) -> bool:
            hyphens = 0
            for index, char in enumerate(token):
                if char.isdigit():
                    return False
                if char == "-":
                    if index == 0 or index == len(token) - 1 or hyphens:
                        return False
                    if not token[index - 1].islower() or not token[index + 1].islower():
                        return False
                    hyphens += 1
                elif char in "!.,":
                    if index != len(token) - 1:
                        return False
                elif not char.islower():
                    return False
            return True

        return sum(valid(token) for token in sentence.split())


if __name__ == "__main__":
    test_cases = [("cat and  dog", 3)]
    for _, (sentence, expected) in enumerate(test_cases):
        assert Solution().countValidWords(sentence) == expected
