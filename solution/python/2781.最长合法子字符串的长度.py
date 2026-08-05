class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        blocked = set(forbidden)
        left = ans = 0
        for right in range(len(word)):
            for size in range(1, min(10, right - left + 1) + 1):
                if word[right - size + 1 : right + 1] in blocked:
                    left = right - size + 2
                    break
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    assert Solution().longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4
