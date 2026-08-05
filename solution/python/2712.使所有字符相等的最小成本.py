class Solution:
    def minimumCost(self, s: str) -> int:
        return sum(
            min(i + 1, len(s) - i - 1) for i in range(len(s) - 1) if s[i] != s[i + 1]
        )


if __name__ == "__main__":
    assert Solution().minimumCost("0011") == 2
