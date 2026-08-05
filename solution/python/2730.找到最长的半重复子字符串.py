class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = pairs = ans = 0
        for right in range(len(s)):
            if right and s[right] == s[right - 1]:
                pairs += 1
            while pairs > 1:
                if s[left] == s[left + 1]:
                    pairs -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    assert Solution().longestSemiRepetitiveSubstring("52233") == 4
