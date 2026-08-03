class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return count * (count + 1) // 2


if __name__ == "__main__":
    test_cases = [(("abada", "a"), 6), (("zzz", "z"), 6)]
    for _, ((s, c), expected) in enumerate(test_cases):
        assert Solution().countSubstrings(s, c) == expected
