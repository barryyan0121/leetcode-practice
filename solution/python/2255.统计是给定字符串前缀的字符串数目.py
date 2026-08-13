"""2255. 统计是给定字符串前缀的字符串数目"""


class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)


if __name__ == "__main__":
    assert Solution().countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc") == 3
