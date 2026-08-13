"""2278. 字母在字符串中的百分比"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


if __name__ == "__main__":
    assert Solution().percentageLetter("foobar", "o") == 33
