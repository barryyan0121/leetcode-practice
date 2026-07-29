class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = 0
        for value in range(2, n + 1):
            if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
                primes += 1

        result = 1
        for value in range(2, primes + 1):
            result = result * value % 1_000_000_007
        for value in range(2, n - primes + 1):
            result = result * value % 1_000_000_007
        return result


if __name__ == "__main__":
    test_cases = [(5, 12), (100, 682289015)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().numPrimeArrangements(n) == expected
