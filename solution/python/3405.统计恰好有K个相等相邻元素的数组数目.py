class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        factorial = [1] * n
        for value in range(1, n):
            factorial[value] = factorial[value - 1] * value % mod
        inverse_factorial = [1] * n
        inverse_factorial[-1] = pow(factorial[-1], mod - 2, mod)
        for value in range(n - 1, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % mod
        combinations = (
            factorial[n - 1] * inverse_factorial[k] * inverse_factorial[n - 1 - k] % mod
        )
        return combinations * m % mod * pow(m - 1, n - k - 1, mod) % mod


if __name__ == "__main__":
    test_cases = [
        ((3, 2, 1), 4),
        ((4, 2, 2), 6),
        ((5, 3, 0), 48),
    ]
    for _, ((n, m, k), expected) in enumerate(test_cases):
        assert Solution().countGoodArrays(n, m, k) == expected
