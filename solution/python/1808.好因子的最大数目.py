class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        mod = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors
        quotient, remainder = divmod(primeFactors, 3)
        if remainder == 1:
            return pow(3, quotient - 1, mod) * 4 % mod
        if remainder == 2:
            return pow(3, quotient, mod) * 2 % mod
        return pow(3, quotient, mod)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxNiceDivisors(5) == 6
    assert solution.maxNiceDivisors(8) == 18
    print("1808 passed")
