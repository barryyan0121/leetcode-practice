class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pairs = {s[index : index + 2] for index in range(len(s) - 1)}
        return any(pair[::-1] in pairs for pair in pairs)


if __name__ == "__main__":
    test_cases = [("leetcode", True), ("abcba", True), ("abcd", False)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().isSubstringPresent(s) == expected
