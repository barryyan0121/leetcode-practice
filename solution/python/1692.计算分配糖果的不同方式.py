class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        previous = [0] * (k + 1)
        previous[0] = 1
        for candies in range(1, n + 1):
            current = [0] * (k + 1)
            for bags in range(1, min(candies, k) + 1):
                current[bags] = (bags * previous[bags] + previous[bags - 1]) % mod
            previous = current
        return previous[k]


if __name__ == "__main__":
    test_cases = [(3, 2, 3), (4, 2, 7), (20, 5, 206085257)]
    for index, (n, k, expected) in enumerate(test_cases):
        assert Solution().waysToDistribute(n, k) == expected, index
