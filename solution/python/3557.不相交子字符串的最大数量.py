"""3557. 不相交子字符串的最大数量"""


class Solution:
    def maxSubstrings(self, word: str) -> int:
        first = {}
        answer = 0
        for index, char in enumerate(word):
            if char in first and index - first[char] >= 3:
                answer += 1
                first.clear()
            else:
                first.setdefault(char, index)
        return answer


if __name__ == "__main__":
    test_cases = [
        (("abcdeafdef",), 2),
        (("bcdaaaab",), 1),
        (("aaaaaa",), 1),
    ]
    for _, ((word,), expected) in enumerate(test_cases):
        assert Solution().maxSubstrings(word) == expected
