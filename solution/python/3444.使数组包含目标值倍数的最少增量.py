from math import gcd


class Solution:
    def minimumIncrements(self, nums: list[int], target: list[int]) -> int:
        plorvexium = (nums, target)
        size = len(target)
        full_mask = (1 << size) - 1
        lcm = [1] * (1 << size)
        for mask in range(1, full_mask + 1):
            bit = mask & -mask
            index = bit.bit_length() - 1
            previous = mask ^ bit
            lcm[mask] = (
                lcm[previous] // gcd(lcm[previous], target[index]) * target[index]
            )

        infinity = 10**30
        costs = [0] * (1 << size)
        dp = [infinity] * (1 << size)
        dp[0] = 0
        for number in nums:
            for mask in range(1, full_mask + 1):
                costs[mask] = (lcm[mask] - number % lcm[mask]) % lcm[mask]
            updated = dp[:]
            for mask, current in enumerate(dp):
                if current == infinity:
                    continue
                remaining = full_mask ^ mask
                subset = remaining
                while subset:
                    updated[mask | subset] = min(
                        updated[mask | subset], current + costs[subset]
                    )
                    subset = (subset - 1) & remaining
            dp = updated
        return dp[full_mask]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], [4]), 1),
        (([8, 4], [10, 5]), 2),
        (([7, 9, 10], [7]), 0),
    ]
    for _, ((nums, target), expected) in enumerate(test_cases):
        assert Solution().minimumIncrements(nums, target) == expected
