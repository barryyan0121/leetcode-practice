class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(left) - ord(right)) for left, right in zip(s, s[1:]))


if __name__ == "__main__":
    test_cases = [("hello", 13), ("zaz", 50)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().scoreOfString(s) == expected
