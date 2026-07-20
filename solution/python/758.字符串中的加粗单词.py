class Solution:
    def boldWords(self, words: list[str], s: str) -> str:
        bold = [False] * len(s)
        for start in range(len(s)):
            for word in words:
                if s.startswith(word, start):
                    bold[start : start + len(word)] = [True] * len(word)

        answer = []
        for index, character in enumerate(s):
            if bold[index] and (index == 0 or not bold[index - 1]):
                answer.append("<b>")
            answer.append(character)
            if bold[index] and (index == len(s) - 1 or not bold[index + 1]):
                answer.append("</b>")
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [
        (["ab", "bc"], "aabcd", "a<b>abc</b>d"),
        (["ab", "cb"], "aabcd", "a<b>ab</b>cd"),
        (["aa"], "aaa", "<b>aaa</b>"),
    ]
    for _, (words, s, expected) in enumerate(test_cases):
        assert Solution().boldWords(words, s) == expected
