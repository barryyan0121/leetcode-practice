class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulo = 1_000_000_007
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = (
                (e + i + u) % modulo,
                (a + i) % modulo,
                (e + o) % modulo,
                i,
                (i + o) % modulo,
            )
        return (a + e + i + o + u) % modulo


if __name__ == "__main__":
    test_cases = [(1, 5), (2, 10), (5, 68)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().countVowelPermutation(n) == expected
