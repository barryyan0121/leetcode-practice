class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split("*")
        for start in range(len(s) - len(prefix) + 1):
            if not s.startswith(prefix, start):
                continue
            end = start + len(prefix)
            if s.find(suffix, end) != -1:
                return True
        return False


if __name__ == "__main__":
    test_cases = [
        (("leetcode", "ee*e"), True),
        (("car", "c*v"), False),
        (("luck", "u*"), True),
    ]
    for _, ((s, p), expected) in enumerate(test_cases):
        assert Solution().hasMatch(s, p) == expected
