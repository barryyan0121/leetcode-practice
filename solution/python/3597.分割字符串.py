"""3597. 分割字符串"""


class Solution:
    def partitionString(self, s: str) -> list[str]:
        seen, parts, start = set(), [], 0
        for end, char in enumerate(s):
            segment = s[start : end + 1]
            if segment not in seen:
                seen.add(segment)
                parts.append(segment)
                start = end + 1
        return parts


if __name__ == "__main__":
    test_cases = [("abbccccd", ["a", "b", "bc", "c", "cc", "d"]), ("aaaa", ["a", "aa"])]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().partitionString(s) == expected
