"""3503. 子字符串连接后的最长回文串 I"""


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        best = 0
        for start_s in range(len(s) + 1):
            for end_s in range(start_s, len(s) + 1):
                left = s[start_s:end_s]
                for start_t in range(len(t) + 1):
                    for end_t in range(start_t, len(t) + 1):
                        candidate = left + t[start_t:end_t]
                        if len(candidate) > best and candidate == candidate[::-1]:
                            best = len(candidate)
        return best


if __name__ == "__main__":
    test_cases = [
        (("a", "a"), 2),
        (("abc", "def"), 1),
        (("b", "a"), 1),
    ]
    for _, ((s, t), expected) in enumerate(test_cases):
        assert Solution().longestPalindrome(s, t) == expected
