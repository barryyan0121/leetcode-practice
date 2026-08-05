"""2002. 两个回文子序列长度的最大乘积"""


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        best = [0] * (1 << n)
        for mask in range(1, 1 << n):
            text = [s[i] for i in range(n) if mask >> i & 1]
            if text == text[::-1]:
                best[mask] = len(text)
        answer = 0
        for mask in range(1, 1 << n):
            other = ((1 << n) - 1) ^ mask
            sub = other
            while sub:
                answer = max(answer, best[mask] * best[sub])
                sub = (sub - 1) & other
        return answer


if __name__ == "__main__":
    test_cases = [(("leetcodecom",), 9)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxProduct(*args) == expected
