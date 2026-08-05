"""3713. 最长的平衡子串 I"""


class Solution:
    def longestBalanced(self, s: str) -> int:
        answer = 0
        for start in range(len(s)):
            counts = [0] * 26
            for end in range(start, len(s)):
                counts[ord(s[end]) - ord("a")] += 1
                nonzero = [count for count in counts if count]
                if len(set(nonzero)) == 1:
                    answer = max(answer, end - start + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(("abbac",), 4), (("zzabccy",), 4), (("aba",), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestBalanced(*args) == expected
