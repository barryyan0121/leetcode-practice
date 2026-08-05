"""1830. 使字符串有序的最少操作次数"""


class Solution:
    def makeStringSorted(self, s: str) -> int:
        mod = 1_000_000_007
        length = len(s)
        factorial = [1] * (length + 1)
        for value in range(1, length + 1):
            factorial[value] = factorial[value - 1] * value % mod
        inverse_factorial = [1] * (length + 1)
        inverse_factorial[length] = pow(factorial[length], mod - 2, mod)
        for value in range(length, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % mod
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        answer = 0
        for index, char in enumerate(s):
            current = ord(char) - 97
            smaller = sum(counts[:current])
            contribution = smaller * factorial[length - index - 1]
            for count in counts:
                contribution = contribution * inverse_factorial[count] % mod
            answer = (answer + contribution) % mod
            counts[current] -= 1
        return answer


if __name__ == "__main__":
    test_cases = [("cba", 5), ("aabaa", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().makeStringSorted(s) == expected
