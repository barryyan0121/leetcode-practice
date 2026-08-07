"""2565. 最少得分子序列"""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(t)
        prefix = [-1] * n
        index = 0
        for i, char in enumerate(s):
            if index < n and char == t[index]:
                prefix[index] = i
                index += 1
        suffix = [len(s)] * n
        index = n - 1
        for i in range(len(s) - 1, -1, -1):
            if index >= 0 and s[i] == t[index]:
                suffix[index] = i
                index -= 1
        answer = n
        right = 0
        for left in range(n + 1):
            if left and prefix[left - 1] < 0:
                break
            right = max(right, left)
            boundary = prefix[left - 1] if left else -1
            while right < n and (
                suffix[right] == len(s) or suffix[right] <= boundary
            ):
                right += 1
            answer = min(answer, right - left)
        return answer


if __name__ == "__main__":
    test_cases = [(("abacaba", "bza"), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumScore(*args) == expected
