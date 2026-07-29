class Solution:
    def lastSubstring(self, s: str) -> str:
        first, second, offset = 0, 1, 0
        while second + offset < len(s):
            if s[first + offset] == s[second + offset]:
                offset += 1
            elif s[first + offset] < s[second + offset]:
                first = max(first + offset + 1, second)
                second = first + 1
                offset = 0
            else:
                second += offset + 1
                offset = 0
        return s[first:]


if __name__ == "__main__":
    test_cases = [("abab", "bab"), ("leetcode", "tcode"), ("aaaa", "aaaa")]
    for _, (value, expected) in enumerate(test_cases):
        assert Solution().lastSubstring(value) == expected
