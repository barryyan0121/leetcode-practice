"""1910. 删除一个字符串中所有出现的给定子字符串"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        length = len(part)
        for char in s:
            result.append(char)
            if len(result) >= length and "".join(result[-length:]) == part:
                del result[-length:]
        return "".join(result)


if __name__ == "__main__":
    assert Solution().removeOccurrences("daabcbaabcbc", "abc") == "dab"
