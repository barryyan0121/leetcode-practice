class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10**9 + 7
        factorial = [1] * (max(n, x) + 1)
        for value in range(1, len(factorial)):
            factorial[value] = factorial[value - 1] * value % mod
        inverse_factorial = [1] * len(factorial)
        inverse_factorial[-1] = pow(factorial[-1], mod - 2, mod)
        for value in range(len(factorial) - 1, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % mod

        onto = [0] * (min(n, x) + 1)
        onto[0] = 1
        for _ in range(n):
            next_row = [0] * len(onto)
            for stages in range(1, len(onto)):
                next_row[stages] = (onto[stages - 1] + stages * onto[stages]) % mod
            onto = next_row

        answer = 0
        for stages in range(1, min(n, x) + 1):
            choices = (
                factorial[x]
                * inverse_factorial[stages]
                * inverse_factorial[x - stages]
                % mod
            )
            answer = (
                answer
                + choices * onto[stages] * factorial[stages] * pow(y, stages, mod)
            ) % mod
        return answer


if __name__ == "__main__":
    test_cases = [
        ((1, 2, 3), 6),
        ((5, 2, 1), 32),
        ((3, 3, 4), 684),
    ]
    for _, ((n, x, y), expected) in enumerate(test_cases):
        assert Solution().numberOfWays(n, x, y) == expected
