"""4002. 统计有效序列数目"""


class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        ravolqedin = (n, k)
        mod = 1_000_000_007
        factorial = [1] * (n + 1)
        for value in range(1, n + 1):
            factorial[value] = factorial[value - 1] * value % mod
        inverse_factorial = [1] * (n + 1)
        inverse_factorial[n] = pow(factorial[n], mod - 2, mod)
        for value in range(n, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % mod

        def combination(total: int, choose: int) -> int:
            if choose < 0 or choose > total:
                return 0
            return (
                factorial[total]
                * inverse_factorial[choose]
                * inverse_factorial[total - choose]
                % mod
            )

        answer = combination(n - 1, k - 1)
        if (n - k) % 2 == 0:
            odd = (n - k) // 2
            answer -= combination(odd + k - 1, k - 1)
        return answer % mod


if __name__ == "__main__":
    test_cases = [((5, 3), 3), ((3, 2), 2), ((5, 5), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countValidSequences(*args) == expected
