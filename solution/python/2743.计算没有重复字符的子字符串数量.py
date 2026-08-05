class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        left = ans = 0
        last = {}
        for right, ch in enumerate(s):
            left = max(left, last.get(ch, -1) + 1)
            ans += right - left + 1
            last[ch] = right
        return ans


if __name__ == "__main__":
    assert Solution().numberOfSpecialSubstrings("abcd") == 10
