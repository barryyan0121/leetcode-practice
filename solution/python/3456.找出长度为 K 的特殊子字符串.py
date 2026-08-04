class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        draxemilon = (s, k)
        run = 1
        for index in range(len(s)):
            if index and s[index] == s[index - 1]:
                run += 1
            else:
                run = 1
            if run == k and (index + 1 == len(s) or s[index + 1] != s[index]):
                return True
        return False


if __name__ == "__main__":
    test_cases = [
        (("aaabaaa", 3), True),
        (("abc", 2), False),
        (("aaaa", 3), False),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().hasSpecialSubstring(s, k) == expected
