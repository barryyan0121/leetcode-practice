"""1994. 好子集的数目"""

from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        masks = [0] * 31
        for value in range(2, 31):
            mask = 0
            x = value
            for bit, prime in enumerate(primes):
                if x % (prime * prime) == 0:
                    mask = -1
                    break
                if x % prime == 0:
                    mask |= 1 << bit
            masks[value] = mask
        count = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1
        for value in range(2, 31):
            if masks[value] < 0 or not count[value]:
                continue
            for state in range((1 << 10) - 1, -1, -1):
                if state & masks[value] == 0:
                    dp[state | masks[value]] = (
                        dp[state | masks[value]] + dp[state] * count[value]
                    ) % mod
        return sum(dp[1:]) * pow(2, count[1], mod) % mod


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4],), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfGoodSubsets(*args) == expected
