class Solution:
    def minimumNumberOfPrimes(self, n: int, m: int) -> int:
        primes = []
        x = 2
        while len(primes) < m:
            for p in primes:
                if p * p > x:
                    primes.append(x)
                    break
                if x % p == 0:
                    break
            else:
                primes.append(x)
            x += 1

        inf = 10**9
        dp = [inf] * (n + 1)
        dp[0] = 0
        for p in primes:
            for s in range(p, n + 1):
                dp[s] = min(dp[s], dp[s - p] + 1)
        return -1 if dp[n] == inf else dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.minimumNumberOfPrimes(10, 2) == 4
    assert s.minimumNumberOfPrimes(9, 3) == 3
    assert s.minimumNumberOfPrimes(1, 1) == -1
    print("3610 ok")
