class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


if __name__ == "__main__":
    assert Solution().minimizedStringLength("aaabc") == 3
