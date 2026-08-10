"""2539. 好子序列的个数"""


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        counts = [s.count(chr(97 + i)) for i in range(26)]
        maximum = max(counts, default=0)
        factorial = [1] * (maximum + 1)
        for value in range(1, maximum + 1):
            factorial[value] = factorial[value - 1] * value % mod
        inverse_factorial = [1] * (maximum + 1)
        inverse_factorial[-1] = pow(factorial[-1], mod - 2, mod)
        for value in range(maximum, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % mod
        answer = 0
        for frequency in range(1, maximum + 1):
            ways = 1
            for count in counts:
                if count >= frequency:
                    combination = (
                        factorial[count]
                        * inverse_factorial[frequency]
                        * inverse_factorial[count - frequency]
                        % mod
                    )
                    ways = ways * (combination + 1) % mod
            answer = (answer + ways - 1) % mod
        return answer


if __name__ == "__main__":
    test_cases = [(("aabb",), 11), (("abcd",), 15)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countGoodSubsequences(*args) == expected
