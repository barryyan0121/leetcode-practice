"""2572. 无平方子集计数"""


class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        modulo = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        masks = {}
        for number in range(2, 31):
            mask = 0
            for index, prime in enumerate(primes):
                if number % (prime * prime) == 0:
                    break
                if number % prime == 0:
                    mask |= 1 << index
            else:
                masks[number] = mask
        dp = [0] * (1 << 10)
        dp[0] = 1
        ones = 0
        for number in nums:
            if number == 1:
                ones += 1
            elif number in masks:
                mask = masks[number]
                for state in range(len(dp) - 1, -1, -1):
                    if state & mask == 0:
                        dp[state | mask] = (dp[state | mask] + dp[state]) % modulo
        return (sum(dp) * pow(2, ones, modulo) - 1) % modulo


if __name__ == "__main__":
    test_cases = [(([3, 4, 4, 5],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().squareFreeSubsets(*args) == expected
