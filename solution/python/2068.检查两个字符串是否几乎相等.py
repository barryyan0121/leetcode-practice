"""2068. 检查两个字符串是否几乎相等"""


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counts = [0] * 26
        for char in word1:
            counts[ord(char) - 97] += 1
        for char in word2:
            counts[ord(char) - 97] -= 1
        return max(map(abs, counts)) <= 3


if __name__ == "__main__":
    test_cases = [(("aaaa", "bccb"), False), (("abcdeef", "abaaacc"), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().checkAlmostEquivalent(*args) == expected
