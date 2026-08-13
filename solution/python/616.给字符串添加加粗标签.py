"""616. 给字符串添加加粗标签"""


class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        bold = [False] * len(s)
        for start in range(len(s)):
            for word in words:
                if s.startswith(word, start):
                    bold[start : start + len(word)] = [True] * len(word)
        result = []
        for index, char in enumerate(s):
            if bold[index] and (index == 0 or not bold[index - 1]):
                result.append("<b>")
            result.append(char)
            if bold[index] and (index == len(s) - 1 or not bold[index + 1]):
                result.append("</b>")
        return "".join(result)


if __name__ == "__main__":
    assert (
        Solution().addBoldTag("abcxyz123", ["abc", "123"]) == "<b>abc</b>xyz<b>123</b>"
    )
    assert Solution().addBoldTag("aaabbb", ["aa", "b"]) == "<b>aaabbb</b>"
