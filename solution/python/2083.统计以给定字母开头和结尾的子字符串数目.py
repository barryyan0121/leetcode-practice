"""2083. 统计以给定字母开头和结尾的子字符串数目"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0] * 26
        answer = 0
        for char in s:
            index = ord(char) - 97
            answer += counts[index] + 1
            counts[index] += 1
        return answer


if __name__ == "__main__":
    test_cases = [("abcba", 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfSubstrings(args) == expected
