"""1930. 长度为 3 的不同回文子序列"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0
        for code in range(26):
            char = chr(code + 97)
            left = s.find(char)
            right = s.rfind(char)
            if left != -1 and left < right:
                answer += len(set(s[left + 1 : right]))
        return answer


if __name__ == "__main__":
    test_cases = [("aabca", 3), ("adc", 0), ("bbcbaba", 4)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().countPalindromicSubsequence(s) == expected
