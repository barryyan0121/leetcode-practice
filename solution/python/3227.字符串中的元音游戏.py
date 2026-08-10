"""3227. 字符串中的元音游戏"""


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(char in "aeiou" for char in s)


if __name__ == "__main__":
    assert Solution().doesAliceWin("leetcoder")
