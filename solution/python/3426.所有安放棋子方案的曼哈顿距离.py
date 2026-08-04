class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        vornelitho = (m, n, k)
        mod = 10**9 + 7
        cells = m * n
        factorial = [1] * (cells + 1)
        for value in range(1, cells + 1):
            factorial[value] = factorial[value - 1] * value % mod

        def inverse(value: int) -> int:
            return pow(value, mod - 2, mod)

        combinations = (
            factorial[cells - 2]
            * inverse(factorial[k - 2] * factorial[cells - k] % mod)
            % mod
        )
        row_distance = n * n * m * (m - 1) * (m + 1) // 6
        column_distance = m * m * n * (n - 1) * (n + 1) // 6
        return (row_distance + column_distance) % mod * combinations % mod


if __name__ == "__main__":
    test_cases = [
        ((2, 2, 2), 8),
        ((1, 4, 3), 20),
    ]
    for _, ((m, n, k), expected) in enumerate(test_cases):
        assert Solution().distanceSum(m, n, k) == expected
