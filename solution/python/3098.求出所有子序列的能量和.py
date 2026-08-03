from bisect import bisect_right


class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        differences = {
            nums[j] - nums[i] for i in range(len(nums)) for j in range(i, len(nums))
        }
        values = sorted(differences)

        def count_at_least(distance: int) -> int:
            dp = [[0] * (k + 1) for _ in nums]
            for i, value in enumerate(nums):
                dp[i][1] = 1
                for size in range(2, k + 1):
                    limit = bisect_right(nums, value - distance, 0, i)
                    dp[i][size] = sum(dp[p][size - 1] for p in range(limit)) % mod
            return sum(row[k] for row in dp) % mod

        counts = [count_at_least(distance) for distance in values]
        answer = 0
        for index, distance in enumerate(values):
            next_count = counts[index + 1] if index + 1 < len(values) else 0
            answer = (answer + distance * (counts[index] - next_count)) % mod
        return answer


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], 3, 4), ([2, 2], 2, 0)]
    for _, (nums, k, expected) in enumerate(test_cases):
        assert Solution().sumOfPowers(nums, k) == expected
