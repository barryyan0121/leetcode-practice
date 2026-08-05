"""2414. 最长的字母序连续子字符串的长度"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        answer = current = 1
        for first, second in zip(s, s[1:]):
            current = current + 1 if ord(second) == ord(first) + 1 else 1
            answer = max(answer, current)
        return answer


if __name__ == "__main__":
    test_cases = [(("abacaba",), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestContinuousSubstring(*args) == expected
