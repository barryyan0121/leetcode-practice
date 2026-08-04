class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]


if __name__ == "__main__":
    test_cases = [(("dart", 3), "tdar"), (("aaa", 1), "aaa")]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().getEncryptedString(s, k) == expected
