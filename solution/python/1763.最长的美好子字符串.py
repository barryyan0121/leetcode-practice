class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        chars = set(s)
        for index, char in enumerate(s):
            if char.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index + 1 :])
                return left if len(left) >= len(right) else right
        return s


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestNiceSubstring("YazaAay") == "aAa"
    assert solution.longestNiceSubstring("Bb") == "Bb"
    assert solution.longestNiceSubstring("c") == ""
    print("1763 passed")
