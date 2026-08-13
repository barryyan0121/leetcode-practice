"""2330. 验证回文串 IV"""


class Solution:
    def makePalindrome(self, s: str) -> bool:
        return sum(a != b for a, b in zip(s, s[::-1])) // 2 <= 2

if __name__ == "__main__":
    assert Solution().makePalindrome("abcdba")
