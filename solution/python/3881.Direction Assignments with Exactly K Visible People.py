MOD = 10**9 + 7
factorial = [1, 1]
inverse = [1, 1]
inverse_factorial = [1, 1]


def ncr(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    while len(inverse) <= n:
        value = len(inverse)
        factorial.append(factorial[-1] * value % MOD)
        inverse.append(inverse[MOD % value] * (MOD - MOD // value) % MOD)
        inverse_factorial.append(inverse_factorial[-1] * inverse[-1] % MOD)
    return factorial[n] * inverse_factorial[n - r] % MOD * inverse_factorial[r] % MOD


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return ncr(n - 1, k) * 2 % MOD


if __name__ == "__main__":
    test_cases = [
        ((3, 1, 0), 2),
        ((3, 2, 1), 4),
        ((1, 0, 0), 2),
    ]
    for _, ((n, pos, k), expected) in enumerate(test_cases):
        assert Solution().countVisiblePeople(n, pos, k) == expected
