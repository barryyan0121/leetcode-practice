from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        limit = 1 << 10
        dp = [10**9] * limit
        dp[0] = 0
        for start in range(k):
            groups = {}
            size = 0
            for index in range(start, len(nums), k):
                groups[nums[index]] = groups.get(nums[index], 0) + 1
                size += 1
            base = min(dp)
            next_dp = [base + size] * limit
            for value, count in groups.items():
                for xor in range(limit):
                    next_dp[xor] = min(next_dp[xor], dp[xor ^ value] + size - count)
            dp = next_dp
        return dp[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minChanges([1, 2, 0, 3, 0], 1) == 3
    assert solution.minChanges([3, 4, 5, 2, 1, 7, 3, 4, 7], 3) == 3
    print("1787 passed")
