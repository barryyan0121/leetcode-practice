class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


if __name__ == "__main__":
    assert Solution().minChanges("1001") == 2
