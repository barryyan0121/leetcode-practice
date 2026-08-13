class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]


if __name__ == "__main__":
    s = Solution()
    assert s.reversePrefix("abcd", 2) == "bacd"
    assert s.reversePrefix("xyz", 3) == "zyx"
    assert s.reversePrefix("hey", 1) == "hey"
